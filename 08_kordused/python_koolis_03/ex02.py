"""
1. Ask the user for a number 10 times and then print the sum of those numbers.
2. Extend this program so that the user is asked for a number until the user no longer enters a new number,
but simply presses the Enter key.
3. Try solving this problem with both a while loop and a for loop.
"""


def ask_for_number_till_use_press_enter() -> int:
    result = 0
    while True:
        number = input("Sisestage arvu: ")
        if number == "":
            break
        elif number.isdigit():
            result += int(number)

    return result


def summarise_unlimited_numbers()-> None:
    result = ask_for_number_till_use_press_enter()
    print(f"Arvude summa on {result}.")


def summarize_limited_numbers()-> None:
    total = 0
    for i in range(10):
        number = input("Sisestage arvu: ")
        if number.isdigit():
            total += int(number)
        else:
            print("Error. Input must be digit")

    print(total)


if __name__ == '__main__':
    choice = input("Valige:\n1 -- Soovite arutada 10 sisestatud numbreid,\n2 -- Soovige arutada nii plaju numbreid kui tahad")
    if choice.isdigit() and choice.strip() == "1":
        summarize_limited_numbers()
    elif choice.isdigit() and choice.strip() == "2":
        summarise_unlimited_numbers()
    else:
        print("Valikud on ainult 1 või 2.")