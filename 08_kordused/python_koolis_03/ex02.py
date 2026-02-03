"""
1. Ask the user for a number 10 times and then print the sum of those numbers.
2. Extend this program so that the user is asked for a number until the user no longer enters a new number,
but simply presses the Enter key.
3. Try solving this problem with both a while loop and a for loop.
"""
import keyboard


def ask_user_for_number ()-> str:
    return input("Sisestage arvu: ")


def summarise_numbers()-> None:
    result = 0
    for number in range(10):
        number = ask_user_for_number()
        result += float(ask_user_for_number())
    print(result)


def ask_for_number_till_use_enter() -> None:
    result = 0
    while ask_user_for_number() != keyboard.is_pressed('Enter'):
        ask_user_for_number()
        result += float(ask_user_for_number())
    print(result)

if __name__ == '__main__':
    summarise_numbers()
