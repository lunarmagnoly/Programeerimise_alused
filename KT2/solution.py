"""
Koosta programm telefoniraamatu loomiseks.


1.       Peab saama sisestada nime ja telefoni numbrit

2.       Samal nimel võib olla ainult üks telefoni number

3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime

a.       Kui vastet pole, siis peab võimaldama lisamist

4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.       Lisa funktsioon terve raamatu kuvamiseks
"""


def check_for_name_and_phone_number(name: str, phone_number: str) -> bool:
    """
    Check if inserted name and phone number exists in phone book
    :return: True of False
    """



def ask_name_and_phone_number():
    """
    Ask name and phone number
    :return:
    """
    name = input("Please enter name: ")
    phone_number = input(" Please enter phone number: ")
    return {name, phone_number}


def add_new_name_and_phone_number(name: str, phone_number: str):
    """
     Add name and phone number
    :return:
    """




def find_phone_number_by_name(name: str) -> str:
    """
    Find phone number by name
    :return: phone_number or " "
    """



def find_name_by_phone_number(phone_number: str) -> str:
    """
    Find name by phone_number
    :return: name or " "
    """


def display_phone_book():
    """Print all names and phones from phone book"""


def display_menu():
    """Display all choices"""
    choice = input("Menu:\n\nInput number of the choise\n\n1 - Add new name and phone number\n2 - Find name by phone number\n"
          "3 - Find phone number by name\n4 - Display phone book")
    return choice



if __name__ == '__main__':
    choose_action = display_menu()
    if choose_action == "1":
        ask_name_and_phone_number()
