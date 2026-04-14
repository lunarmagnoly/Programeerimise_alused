"""
Task 7 – Estonian Personal Identification Code

This program analyzes Estonian personal identification codes (isikukood).
The personal code consists of 11 digits and is processed as a string.

The program:
- validates the format of the personal code
- extracts and validates the birthdate
- determines the birth year
- checks the control number using modulo 11 algorithm
- determines whether the personal code is valid

The program uses string operations for analysis.
Several personal codes can be defined directly in the code for testing
by commenting or uncommenting them.

The solution also follows the official structure of Estonian personal codes
and avoids invalid dates and incorrect control numbers.
"""


import calendar
from random import randint


def check_format(personal_code: str) -> bool:
    """
    Checks the format of Estonian personal code
    (length, digits only, first number from 1 to 6).

    :param personal_code: str
    :return: bool
    """
    personal_code = personal_code.strip()
    if len(personal_code) == 11 and personal_code.isdigit():
        return personal_code[0] in {"1", "2", "3", "4", "5", "6"}
    return False


def get_birthyear(personal_code: str) -> int:
    """
    Extracts birth year from Estonian personal code.

    :param personal_code: str
    :return: int, birth year or -1 if invalid
    """

    if check_format(personal_code):
        personal_code = personal_code.strip()
        if int(personal_code[0]) in {1,2}:
            return 1800 + int(personal_code[1:3])
        elif int(personal_code[0]) in {3,4}:
            return 1900 + int(personal_code[1:3])
        elif int(personal_code[0]) in {5,6}:
            return 2000 + int(personal_code[1:3])
    return -1


def check_data(personal_code: str) -> bool:
    """
    Checks the birthdate in Estonian personal code.

    Validates month and day values, including February
    and leap year rules.

    :param personal_code: str
    :return: bool
    """

    if check_format(personal_code):
        if get_birthyear(personal_code) != -1:
            personal_code = personal_code.strip()
            birth_month = int(personal_code[3: 5])
            birth_day = int(personal_code[5: 7])
            if 1 <= birth_month <= 12:
                if birth_month in {1, 3, 5, 7, 8, 10, 12} and 1 <= birth_day <= 31:
                    return True
                elif birth_month in {4, 6, 9, 11} and 1 <= birth_day <= 30:
                    return True
                elif birth_month == 2 and 1 <= birth_day <= 29 and calendar.isleap(get_birthyear(personal_code)):
                    return True
                elif birth_month == 2 and 1 <= birth_day <= 28 and  not calendar.isleap(get_birthyear(personal_code)):
                    return True
    return False


def check_control(personal_code: str) -> bool:
    """
    Validates the control number of Estonian personal code.

    The control number is calculated from the first 10 digits
    using modulo 11 algorithm with two weight sequences.

    :param personal_code: str
    :return: bool
    """

    personal_code = personal_code.strip()

    if check_format(personal_code):
        weight = "1234567891"
        control_number1 = int(calculate_control_number(personal_code, weight))
        if control_number1 != -1:
            if control_number1 < 10:
                return control_number1 == int(personal_code[10])
            elif control_number1 == 10:
                weight = "3456789123"
                control_number2 = int(calculate_control_number(personal_code, weight))
                if control_number2 < 10 and control_number2 != -1:
                    return control_number2 == int(personal_code[10])
                if control_number2 == 10:
                    return int(personal_code[10]) == 0
    return False


def is_valid_personal_code(personal_code: str) -> bool:
    """
    Checks if Estonian personal code is valid.

    :param personal_code: str
    :return: bool
    """

    return check_data(personal_code) and check_control(personal_code)


def get_random_gender()-> int:
    """ Generates random gender number from 1 to 6"""
    return randint(1,6)


def get_random_year_part()-> int:
    """ Generates random year_part from 0 to 99"""
    return randint(0, 99)

def get_random_month()-> int:
    """ Generates random month from 1 to 12"""
    return randint(1, 12)


def get_random_year(gender, year_part)-> int:
    """
    Get full random birth_year

    param: int
    return: int
    """

    if gender in {1, 2}:
        return 1800 + year_part
    if gender in {3, 4}:
        return 1900 + year_part
    if gender in {5, 6}:
        return 2000 + year_part
    return -1


def get_random_day(month: int, year: int) -> int:
    """
    Get random birth_day depending on the month

    param: int
    return: int in case error -1
    """
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return randint(1,31)
    if month in {4, 6, 9, 11}:
        return randint(1,30)
    if month == 2 and calendar.isleap(year):
        return randint(1,29)
    if month == 2 and not calendar.isleap(year):
        return randint(1, 28)
    return -1


def get_serial_number() -> int:
    """Get random serial number"""
    return randint(1,999)


def first10() ->str:
    """Combine all data to string"""
    gender = get_random_gender()
    year_part = get_random_year_part()
    full_year = get_random_year(gender,year_part)
    month = get_random_month()
    day = get_random_day(month, full_year)
    serial_number = get_serial_number()
    return (str(gender) +
            str(year_part).zfill(2) +
            str(month).zfill(2) +
            str(day).zfill(2) +
            str(serial_number).zfill(3))


def calculate_control_number(code10: str, weight: str)-> str:
    """Calculate valid control number"""
    code10 = code10.strip()
    weight = weight.strip()
    code10_digits = []
    weight_digits = []
    total = 0
    if code10.isdigit() and weight.isdigit():
        for ch in code10:
            code10_digits.append(int(ch))

        for ch in weight:
            weight_digits.append(int(ch))

        for i in range(10):
            pc = code10_digits[i] * weight_digits[i]
            total += pc
        return str(total % 11)
    return "Viga"


def generate_valid_personal_code()-> str:
    """Generate valid personal code"""
    weight = "1234567891"
    code10 = first10()
    control_number1 = int(calculate_control_number(code10, weight))
    if control_number1 < 10:
        return code10 + str(control_number1)
    elif control_number1 == 10:
        weight = "3456789123"
        control_number2 = int(calculate_control_number(code10, weight))
        if control_number2 < 10:
            return code10 + str(control_number2)
        if control_number2 == 10:
            return code10 + "0"
    return "Viga"


def get_gender(personal_code: str) -> str:
    """Get person's gender from personal code"""
    gender = ""
    if is_valid_personal_code(personal_code):
        if int(personal_code[0]) in {1, 3, 5}:
            gender = "mees"
        if int(personal_code[0]) in {2, 4, 6}:
            gender = "naine"
    return gender


def get_birthmonth(personal_code: str) -> str:
    """Get person's birthmonth from personal code"""
    if is_valid_personal_code(personal_code):
        return personal_code[3:5]
    return "Isikukood peab olema korrektne"

def get_birthday(personal_code:str) -> str:
    """Get person's birthday from personal code"""
    if is_valid_personal_code(personal_code):
        return personal_code[5:7]
    return "Isikukood peab olema korrektne"

def decode_personal_code(personal_code: str) -> str:
    """Decode Estonian personal identification code"""
    if is_valid_personal_code(personal_code):
        gender = get_gender(personal_code)
        year = get_birthyear(personal_code)
        month = get_birthmonth(personal_code)
        day = get_birthday(personal_code)
        birthday = day + "." + month + "." + str(year)
        return f"Isikukoodi omanik on {gender} kelle sünnipäev on {birthday}"
    return "Ei saa dekodeerida ebakorrektne kood"



if __name__ == '__main__':
    print("Valikud:")
    choice_input = input("1-Kontrolli kas isikukood on korrektne. \n2-Genereeri korrektne isikukood.\n3-Isikukoodi dekodeerimine\n")
    if choice_input.strip() == "1":
        personal_code_input = input("Sisestage isikukood: ").strip()
        if is_valid_personal_code(personal_code_input):
            print("Isikukood on korrektne")
        else:
            print("Isikukood ei ole korrektne")
    elif choice_input.strip() == "2":
        print(generate_valid_personal_code())
    elif choice_input.strip() == "3":
        personal_code_input = input("Sisestage isikukood: ").strip()
        print(decode_personal_code(personal_code_input))