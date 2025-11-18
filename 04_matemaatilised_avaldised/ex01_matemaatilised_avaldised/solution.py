"""Math exercises."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * radius ** 2
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = (math.sqrt(3) / 4) * (side_length ** 2)
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b * b - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a * a + b * b)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c * c - a * a)
    return b


if __name__ == '__main__':
    addition_result, difference = sum_and_difference(5, 6)
    assert addition_result == 11
    assert difference == -1

    float_division_result = float_division(10, 2)
    assert isinstance(float_division_result, float)
    assert 4.99 < float_division_result < 5.01

    integer_division_result = integer_division(10, 3)
    assert isinstance(integer_division_result, int)
    assert integer_division_result == 3
    integer_division_result = integer_division(10, 10)
    assert integer_division_result == 1

    multiply_numbers, power, remainder = powerful_operations(2,2)
    assert multiply_numbers == 4
    assert power == 4
    assert remainder == 0

    find_average_result = find_average(3, 4)
    assert isinstance(find_average_result, float)
    assert 3,49 < find_average_result < 3.51

    area_of_a_circle_result = area_of_a_circle(5)
    assert 78.53 < area_of_a_circle_result < 78.55, f"{area_of_a_circle_result}" # need to check if round was used

    area_of_an_equilateral_triangle_result = area_of_an_equilateral_triangle(3)
    assert isinstance(area_of_an_equilateral_triangle_result, int)
    assert area_of_an_equilateral_triangle_result == 4

    calculate_discriminant_result = calculate_discriminant(-1, 2,3)
    assert isinstance(calculate_discriminant_result, int)
    assert calculate_discriminant_result == 16

    calculate_hypotenuse_length_result = calculate_hypotenuse_length(3, 4)
    assert isinstance(calculate_hypotenuse_length_result, float)
    assert 4.99 < calculate_hypotenuse_length_result < 5.01

    calculate_cathetus_length_result = calculate_cathetus_length(4, 5)
    assert isinstance(calculate_cathetus_length_result, float)
    assert 2.99 < calculate_cathetus_length_result < 3.01