import random
import os

def clear_console():
    os.system("cls")

def swap_operators(operator: str) -> str:
    return operator.translate(str.maketrans({
        "×": "*",
        "*": "×",
        "÷": "/",
        "/": "÷"
    }))

    # mapping = {
    #     "×": "*",
    #     "*": "×",
    #     "÷": "/",
    #     "/": "÷"
    # }

    # for k, v in mapping.items():
    #     operator = operator.replace(k, v)
    
    # return operator

def get_rand(length: int) -> int:
    """
    Get random didget based off length
    """
    min = 10 ** (length - 1)
    max = 10 ** length - 1
    return random.randint(min, max)

def generate_calculation(didgets1: int, didgets2: int, operator: str) -> object:
    """
    Generate a 2 numbered calculation with a custom operator
    """
    first_didget = get_rand(didgets1)
    second_didget = get_rand(didgets2)

    if len(operator) != 1:
        print("Operator is invalid:", operator)
        return
    
    calculation = " ".join([
        str(first_didget), 
        str(operator),
        str(second_didget)
    ])
    answer = eval(calculation)

    return calculation, answer


clear_console()
didgets_1 = int(input("Enter length (1): "))
didgets_2 = int(input("Enter length (2): "))

clear_console()

operator_mapping = {
    1: "+",
    2: "-",
    3: "×",
    4: "**",
    5: "÷"
}

for x, y in operator_mapping.items():
    print(f"[{x}] {y}")

operator = int(input("Enter operator: "))
operator = operator_mapping.get(operator)
operator = swap_operators(operator)
print(operator)

while True:
    # Generate Question
    clear_console()
    calculation, answer = generate_calculation(didgets_1, didgets_2, operator)
    print(calculation, "=")
    input("Press enter to reveal answer..")

    # Show Answer
    clear_console()
    print(calculation, "=", answer)
    input("Press enter to generate a new question..")
