import time
import pyperclip
import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

def handle_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except:
        print("⚠️ Only numbers can be entered")
        return 0

formats = {
    1: [ "<t:{unix}:R>", "4 months ago" ],
    2: [ "<t:{unix}:D>", "1 January 2026" ],
    3: [ "<t:{unix}:T>", "00:00:00" ],
    4: [ "<t:{unix}:t>", "00:00" ],
    5: [ "<t:{unix}:F>", "Thursday, 1 January 2026 00:00" ]
}

unix_type = {
    1: "Time add DD/MM/YYYY + HH:MM:SS",
    2: "Time set DD/MM/YYYY + HH:MM:SS"
}

def main():
    unix = "0"

    # Select UNIX type
    print("Select an option")
    for key, line in unix_type.items():
        print(f"[{key}] {line}")

    selected = handle_input("» Enter an option: ")
    match selected:
        case 1:
            unix = round((datetime.now() + relativedelta(
                days=handle_input(" » Days: "),
                months=handle_input(" » Months: "),
                years=handle_input(" » Years: "),
                hours=handle_input(" » Hours: "),
                minutes=handle_input(" » Minutes: "),
                seconds=handle_input(" » Seconds: ")
            )).timestamp())
        case 2:
            unix = round(datetime(
                day=handle_input(" » Day: "),
                month=handle_input(" » Month: "),
                year=handle_input(" » Year: "),
                hour=handle_input(" » Hour: "),
                minute=handle_input(" » Minute: "),
                second=handle_input(" » Second: ")
            ).timestamp())
        case _:
            print("Invalid option")
            return

    # Select which format to copy
    print()
    print("Select an option")
    for key, line in formats.items():
        formatted_line = str(line[0]).replace("{unix}", f"{unix}")
        print(f"[{key}] {formatted_line} | {line[1]}")

    while True:
        selected = handle_input("» Enter an option: ")
        selected = formats.get(selected)[0].replace("{unix}", f"{unix}")
        try:
            pyperclip.copy(selected)
        except Exception as err:
            print("Error copying to clipboard:", err)
            return
        print("Successfully copied to clipboard")


while True:
    main()
    input("Press enter to restart...")
