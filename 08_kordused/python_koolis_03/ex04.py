

"""
Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni.

1. jätta meelde suvaline arv 1-20
2. korda
    küsi kasutajalt arvu
        ütle, kas suurem
        ütle, kas väiksem
        ütle, Õige ja lõpeta
"""

from random import randint

def play_guessing_game():
    correct = randint(1,20)
    tries = 0
    while tries < 5:
        answer = int(input(f"Katse {tries + 1}. Sisesta arv vahemikus 1-20: "))
        if answer > correct:
            print("Liiga suur, proovi uuesti.")
            continue
        if answer < correct:
            print("Liiga väike, proovi uuesti.")
            continue
        print(f"Tubli, arvasid ära. Arv oli {correct}")
        break
    else:
        print(f"Katset said otsa. Õige vastus on {correct}")

if __name__ == '__main__':
    play_guessing_game()