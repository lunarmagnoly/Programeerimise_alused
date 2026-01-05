

"""Calculate the perimeter and area of a rectangle."""

def rectangle_perimeter(height: float, length: float)-> float:
    """Calculate rectangle perimeter"""
    return (height + length) * 2


def rectangle_area(height: float, length: float)-> float:
    """Calculate rectangle area"""
    return height * length

if __name__ == '__main__':
    ask_rectangle_height = float(input("Mis on ristküliku kõrgus? "))
    ask_rectangle_length = float(input("Mis on ristküliku pikkus? "))
    print(f"Ristküliku ümbermõõt on {rectangle_perimeter(ask_rectangle_height, ask_rectangle_length)} ja pindala on {rectangle_area(ask_rectangle_height, ask_rectangle_length)}")