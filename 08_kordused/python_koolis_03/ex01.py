"""
 1. ask the user for their name and
 2. greet them by name 5 times, also adding a sequence number to the greeting.
"""


def greet_user_5_times():
    ask_user_name = input("Sisesta oma nimi: ")
    count = 0
    for i in range(5):
        count += 1
        print(f"Ole tervitatud, {ask_user_name}, {count}. korda.")


if __name__ == '__main__':
    greet_user_5_times()