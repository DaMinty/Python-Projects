import subprocess
import os

def clear_console():
    os.system("cls")

def run_command(command_parts: list[str]) -> tuple[bool, str]:
    command = " | ".join(command_parts)
    
    try:
        raw_data = subprocess.check_output(command, shell=True)
        data = raw_data.decode()
    except Exception as err:
        sanitized_error = str(err)
        sanitized_error = sanitized_error.split("'")[2]
        sanitized_error = sanitized_error.title()
        sanitized_error = sanitized_error.strip()
        return False, sanitized_error
    
    return True, data

def get_all_ssid() -> tuple[bool, dict[int, str]]:
    # Get SSIDs
    success, result = run_command([
        "netsh wlan show profiles",
        "findstr \"All\""
    ])

    if success:
        # Sanitize
        data = str(result)
        data = data.split("\r\n")
        
        # Sort Profiles
        profiles = {}

        for i, profile in enumerate(data, 1):
            if profile:
                profile = profile.split(":")[1]
                profile = profile.strip()
                profiles.update({ i: profile })

        profiles.update({
            99: "Free-Wifi"
        })
    else: return False, result

    return True, profiles

def get_password(ssid: str) -> tuple[bool, str]:
    # Get Password from SSID
    success, result = run_command([
        f"netsh wlan show profile \"{ssid}\" key=clear",
        "findstr \"Key Content\""
    ])
    
    if success:
        # Sanitize
        sanitized_data = str(result)
        sanitized_data = sanitized_data.split(":")[1]
        sanitized_data = sanitized_data.strip()
        
        return True, sanitized_data
    else:
        return False, result

def main():
    # Select Profile
    success, ssid_result = get_all_ssid()
    if success:
        clear_console()
        print()
        print("Select a profile")
        print()
        print("[0] Show All")
        for inc, profile in ssid_result.items():
            print(f"[{inc}] {profile}")
        print()
    else:
        print("Error fetching profiles: " + ssid_result)


    # Show Password
    try: profile_input = int(input("Select a profile: "))
    except: print("Input Error: Input requires integer"); return

    if profile_input == 0:
        clear_console()
        print()
        print("Loading all passwords..")
        print()
        for inc, profile in ssid_result.items():
            success, psswrd_result = get_password(profile)
            if success:
                print(f"{profile} : {psswrd_result}")
            else:
                print(f"Error loading profile {profile}: {psswrd_result}")
        print()            
    else:
        try: profile = ssid_result[profile_input]
        except: print("Input Error: Out of range"); return
        
        success, psswrd_resut = get_password(profile)
        if success:
            clear_console()
            print()
            print(f"SSID: '{profile}'")
            print(f"Password: '{psswrd_resut.strip()}'")
            print()
        else:
            print("Error fetching password: " + psswrd_resut)

if __name__ == "__main__":
    while True:
        main()
        input("Press Enter to Continue..")
