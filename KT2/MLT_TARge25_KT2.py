"""
Koosta programm telefoniraamatu loomiseks.


1.       Peab saama sisestada nime ja telefoni numbrit

2.       Samal nimel võib olla ainult üks telefoni number

3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime

a.       Kui vastet pole, siis peab võimaldama lisamist

4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.       Lisa funktsioon terve raamatu kuvamiseks
"""


def load_phone_book_from_file(filename:str) -> dict:
    """
    Load phone book from file to dictionary
    :param filename: address of file where we get our phone book from
    :return: dict: dictionary of names and phone numbers from file
    """
    phone_book = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                name, phone_number = line.split()
                phone_book[name] = phone_number
    except FileNotFoundError:
        return {}
    return phone_book


def save_phone_book_to_file(phone_book, filename) -> None:
    """
    Save phone book updates to file
    :param phone_book: dictionary where names and phone numbers are saved
    :param filename: file for dictionary backup
    :return None
    """
    with open(filename, "w", encoding="utf-8") as f:
        for name, phone_number in phone_book.items():
            f.write(f"{name} {phone_number}\n")


def ask_name() -> str:
    """
    Ask name
    :return: entered name
    """
    return input("Please enter name: ")


def ask_number()-> str:
    """
    Ask phone number
    :return: entered phone number
    """
    return input("Please enter phone number: ")


def ask_name_and_phone_number() -> tuple[str,str]:
    """
    Ask name and phone number
    :return: entered name and phone number
    """
    return ask_name(), ask_number()


def add_new_name_and_phone_number(phone_book: dict) -> bool:
    """
    Add name and phone number
    :param phone_book: the phone book where to we add the name and the phone number
    :return: bool True if data was added, False if not
    """
    name, phone_number = ask_name_and_phone_number()
    if name not in phone_book:
        phone_book[name] = phone_number
        print("New name and phone number added.")
        return True
    print(f"{name} already exists in phone book.")
    return False

def add_and_save_new_name_and_number(phone_book: dict, filename: str):
    """
    If name and number were added to the phone book, save new data to file
    :param phone_book: the dictionary that was updated
    :param filename: the file that will be updated if needed
    :return: None
    """
    if add_new_name_and_phone_number(phone_book):
        save_phone_book_to_file(phone_book,filename)


def find_phone_number_by_name(name: str, phone_book: dict) -> str:
    """
    Find phone number by name
    :param name: what name do we seek
    :param phone_book: where do we seek the phone number
    :return: phone_number or " " if the name is absent
    """
    if name in phone_book:
        return phone_book[name]
    return " "


def find_name_by_phone_number(phone_number: str, phone_book: dict) -> str:
    """
    Find name by phone number
    :param phone_number: what phone number do we seek
    :param phone_book: where do we seek the phone number
    :return: name or " " if the phone_number is absent
    """
    for name, number in phone_book.items():
        if number == phone_number:
            return name
    return " "


def display_phone_book(phone_book: dict) -> None:
    """
    Print all names and phones from phone book
    :param phone_book: the phone book in question
    :return: None
    """
    for name, phone_number in phone_book.items():
        print(name, phone_number)

def display_menu() -> str:
    """Display menu"""
    choice = input("\nMenu:\n\nInput number of the choise\n\n1 - Add new name and phone number\n2 - Find name by phone number\n"
          "3 - Find phone number by name\n4 - Display phone book\n5 - Close program\n\nChoice: ")
    return choice


if __name__ == '__main__':
    filename = "phone_book.txt"
    phone_book = load_phone_book_from_file(filename)
    while True:
        choose_action = display_menu()
        if choose_action == "1":
            add_and_save_new_name_and_number(phone_book, filename)
        elif choose_action == "2":
            phone_number = ask_number()
            name = find_name_by_phone_number(phone_number, phone_book)
            if name != " ":
                print(f"Phone number {phone_number} belongs to {name}")
            else:
                new_choice = input(f"Phone book has no one with phone number {phone_number}. Would you like to add it? (y/n)")
                if new_choice.strip().lower() == "y":
                    add_and_save_new_name_and_number(phone_book, filename)
        elif choose_action == "3":
            name = ask_name()
            phone_number = find_phone_number_by_name(name, phone_book)
            if phone_number != " ":
                print(f"{name} phone number is {phone_number}")
            else:
                new_choice = input(f"Phone book has no one with name {name}. Would you like to add it? (y/n)")
                if new_choice.strip().lower() == "y":
                    add_and_save_new_name_and_number(phone_book, filename)
        elif choose_action == "4":
            display_phone_book(phone_book)
        elif choose_action == "5":
            break
