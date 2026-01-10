

"""
Create a program that asks the user for a number N and prints an N×N square made of the letter "O".

Then modify the program so that the characters on the square’s diagonals are "X".
"""

def draw_square(size: int, symbol: str, alt: str):
    for row in range(size):
        for col in range(size):
            if row == col or row + col == size - 1:
                print(f"{alt}", end=" ")
            else:
                print(f"{symbol}", end = " ")
        print()


if __name__ == '__main__':
    size = int(input("Sisesta ruudude suurus: "))
    draw_square(size, "O", "X")
    print()
    draw_square(size * 2, "I", "-")