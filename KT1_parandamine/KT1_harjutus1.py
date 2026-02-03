"""
A mantra is a syllable, word, phrase, or sound used in meditation in many Eastern religions.
A mantra is repeated for as long as is deemed necessary.
Write a program that:
 1.asks the user for a phrase they want to use as a mantra,
 2.asks the user how many times they want to repeat the mantra,
 3.displays the mantra entered by the user on the screen the same number of times.
"""


def display_mantra_asked_number_of_times():
    """
    Ask for mantra phrase,
    Ask how many times mantra is repeated,
    Display said mantra phrase said number of times.
    """
    mantra_phrase = input("Enter phrase that will be used as mantra: ")
    mantra_is_repeated = int(input("How many times mantra will be repeated? Insert positive integer number "))
    count = 1
    while mantra_is_repeated >= 0 and mantra_is_repeated.is_integer() and count <= mantra_is_repeated :
        print(count, mantra_phrase)
        count += 1


if __name__ == '__main__':
    display_mantra_asked_number_of_times()