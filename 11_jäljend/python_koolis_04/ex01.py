"""
Create a list of numbers with at least 10 numbers.
Create a program that ask the user for a multiplier,
multiplies all numbers in the original list by it and prints the result.
"""
from random import randint


def generate_number_list( smallest: int, largest:int)-> list[int]:
    result = []
    for i in range(10):
        random_number = randint(smallest, largest)
        result.append(random_number)
    return result

def ask_user_int(question: str) ->int:
    user_input = input(question).strip()
    while not user_input.isdigit():
        print("Input is not an integer. Please try again.")
        user_input = input(question).strip()
    return int(user_input)


def multiply_list(numbers: list[int], multiplier: int):
    result = []
    for number in numbers:
        result.append(number * multiplier)
    return result


def show_result(original_numbers: list[int], multiplier, result_numbers: list[int]):
    for i in range(len(original_numbers)):
        print(f"{original_numbers[i]} * {multiplier} = {result_numbers[i]}")


if __name__ == '__main__':
    numbers_list = generate_number_list(1, 10)
    print(numbers_list)
    multiplier = ask_user_int("Please enter multiplier: ")
    print(f"{multiplier}")
    multiplied_list = multiply_list(numbers_list, multiplier)
    print(multiplied_list)
    print(show_result(numbers_list, multiplier, multiplied_list))
