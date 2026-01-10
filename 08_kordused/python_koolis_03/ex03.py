

"""
Create a program that helps children practice addition.
The program should present addition problems with random numbers and wait for the user's answer.
If the answer is correct, the program should praise the user; if it is incorrect, the program should
show the correct answer and present a new problem.

The number of problems to be presented can be predefined in the program (for example, 10),
and the range of numbers used can also be predefined (for example, from 1 to 50).
The program should keep track of correct answers and display the final result after the last problem.

Optional extensions:

The program allows the user to enter how many problems they want to solve.
The user can define the range of numbers (maximum or both minimum and maximum).
The program asks not only addition problems but also other operations
(subtraction, multiplication, division).
Based on the final result, the program responds differently, for example:
"Excellent!", "Well done!", "Average result!", "Try harder next time.", etc.
"""

from random import randint, choice

operations = ["+", "-", "*", "**", "//"]
true_answers_reactions = ["Ülihea!", "Tubli!", "Hea vastus!"]
false_answers_reactions = ["Vale vastus.", "Harjuta rohkem.", "Püüa järgmisel korral rohkem."]

def get_calculation(min_value: int, max_value: int) -> tuple[str, int]:
    num1 = randint(min_value, max_value)
    num2 = randint(min_value, max_value)
    operation = choice(operations)
    if operation == "+":
        correct_answer = num1 + num2
        return f"{num1} + {num2} = ", correct_answer
    elif operation == "-":
        correct_answer = num1 - num2
        return f"{num1} - {num2} = ", correct_answer
    elif operation == "*":
        correct_answer = num1 * num2
        return f"{num1} * {num2} = ", correct_answer
    elif operation == "**":
        correct_answer = num1 ** num2
        return f"{num1} ** {num2} = ", correct_answer
    elif operation == "//":
        correct_answer = num1 // num2
        return f"{num1} // {num2} = ", correct_answer
    return "Tundmatu tehe", 0


def test_user_knowledge(min_value: int, max_value: int) -> tuple[bool, int]:
    calculation, correct_answer = get_calculation(min_value, max_value)
    user_answer = int(input(calculation))
    return user_answer == correct_answer, correct_answer


def practice_addition(count: int, min_value: int, max_value: int) -> None:
    correct_count = 0

    for i in range(count):
        true_answers_reaction = choice(true_answers_reactions)
        false_answers_reaction = choice(false_answers_reactions)
        print(f"Harjutus {i+1}/{count}")
        is_answer_correct, correct_answer = test_user_knowledge(min_value, max_value)
        if is_answer_correct:
            print(f"{true_answers_reaction} Vastasid õigesti.")
            correct_count+=1
        else:
            print(f"{false_answers_reaction} Õige vastus on {correct_answer}.")
    print(f"See oli viimane ülesanne. Kogusid {count}-st punkrist {correct_count}.")


if __name__ == '__main__':
    min_value = int(input("Milline peab olema minimaalne täisarvu väärtus? "))
    max_value = int(input("Milline peab olema maksimaalne täisarvu väärtus? "))
    count = int(input("Mitu korda soovid harjutada? "))
    practice_addition(count, min_value, max_value)

