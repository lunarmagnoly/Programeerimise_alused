"""Math exercises vol2."""
import math


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = math.sin(math.radians(angle))
    sine = round(sine, 1)
    cosine = math.cos(math.radians(angle))
    cosine = round(cosine, 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers

if __name__ == '__main__':
    time_converter_result = time_converter(13590)
    assert isinstance(time_converter_result, str)
    assert time_converter_result == "13590 sekundit on 3 tund(i) ja 46 minut(it)."

    student_helper_result = student_helper(90)
    assert isinstance(student_helper_result, str)
    assert student_helper_result == "Nurk: 90, siinus: 1.0, koosinus: 0.0.", f"{student_helper(90)}"
    student_helper_result = student_helper(180)
    assert isinstance(student_helper_result, str)
    assert student_helper_result == "Nurk: 180, siinus: 0.0, koosinus: -1.0.", f"{student_helper(180)}"
    student_helper_result = student_helper(30)
    assert isinstance(student_helper_result, str)
    assert student_helper_result == "Nurk: 30, siinus: 0.5, koosinus: 0.9.", f"{student_helper(30)}"

    greetings_result = greetings(5)
    assert isinstance(greetings_result, str)
    assert greetings_result == "HeyHeyHeyHeyHey", f"{greetings(5)}"

    adding_numbers_result = adding_numbers(5, 7)
    assert isinstance(adding_numbers_result, str)
    assert adding_numbers_result == "57"