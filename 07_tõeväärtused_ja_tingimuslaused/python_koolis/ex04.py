

"""
Create a mathematical dog (M-Koer) program.
Ask for two numbers and an operator and print the result as barking ("auh").
"""

def simple_calculator(number1: int, number2: int, operator: str) -> int:
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    if operator == "*":
        return number1 * number2
    if operator == "/":
        return round(number1 / number2)
    return -1

if __name__ == '__main__':
    input_number1 = int(input("Sisestage esimene arv: "))
    input_number2 = int(input("Sisestage teine arv: "))
    input_operator = input("Sisestage tehe: ")
    calculation_result = simple_calculator(input_number1, input_number2, input_operator)
    if calculation_result >= 0:
        print(calculation_result*"auh ")
    else:
        print("Kontrollige operaatori õigust. Koer ei saa haukuda negatiivset arvu.")