"""
1. Ask the user for 3 numbers

2. Multiply the smallest number by two

3. Ask the user for the squares of numbers from 1 up to the result of the previous step (loop)

4. Tell whether the user answered correctly or incorrectly

5. Tell how many times the user answered correctly
"""
def find_smallest_number() -> int:
    smallest_number = int(input("Sisesta number: "))
    for number in range(2):
        input_number = int(input("Sisesta number: "))
        if smallest_number > input_number:
            smallest_number = input_number
    return smallest_number


def multiply_smallest_number_by_2() -> int:
    smallest_number = find_smallest_number()
    return smallest_number * 2


def check_if_user_is_correct() ->None:
    count = 0
    limit = multiply_smallest_number_by_2()
    for number in range(1, limit + 1, 1):
        ask_user_answer = int(input(f"How much is {number} ^ 2 "))
        correct_answer = number ** 2
        if ask_user_answer == correct_answer:
            count += 1
            print(f"Correct. {count} / {limit}")
        else:
            print(f"Wrong. {count} / {limit}")


if __name__ == '__main__':
    check_if_user_is_correct()