

"""
Create a guessing game where the player has to guess an integer chosen by the computer
between 1 and 20.

The program randomly selects a number from 1 to 20.
The user is asked to guess the number.
After each guess, the program tells whether the guess is too high or too low.
If the guess is correct, the program congratulates the user and ends the game.

Extend program so that the user has 5 chances to guess the number,
i.e. if they don't guess within 5 attempts, the computer will say they lost and report the correct number.
Extend the block diagram accordingly.
"""

from random import randint

def play_guessing_game():
    correct = randint(1,20)
    tries = 0
    while tries < 5:
        answer = int(input(f"Katse {tries + 1}. Sisesta arv vahemikus 1-20: "))
        if answer > correct:
            print("Liiga suur, proovi uuesti.")
            tries += 1
            continue
        if answer < correct:
            print("Liiga väike, proovi uuesti.")
            tries += 1
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct}")
        break
    else:
        print(f"Katset said otsa. Õige vastus on {correct}")

if __name__ == '__main__':
    play_guessing_game()