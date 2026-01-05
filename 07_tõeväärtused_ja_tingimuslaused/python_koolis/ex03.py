

"""
Create a simple calculator
Ask for 2 numbers and operator
Print the calculation and result
"""

def simple_calculator(number1: float, number2: float, operator: str) -> str:
    if operator == "+":
        return f"{number1} + {number2} = {number1 + number2}"
    if operator == "-":
        return f"{number1} - {number2} = {number1 - number2}"
    if operator == "*":
        return f"{number1} * {number2} = {number1 * number2}"
    if operator == "/":
        return f"{number1} / {number2} = {number1 / number2}"
    return "Operators are +, - , *, /"


if __name__ == '__main__':
    input_number1 = int(input("Sisestage esimene arv: "))
    input_number2 = int(input("Sisestage teine arv: "))
    input_operator = input("Sisestage tehe: ")
    print(simple_calculator(input_number1, input_number2, input_operator))