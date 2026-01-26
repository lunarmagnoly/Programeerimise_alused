"""
1. Create a list of at least ten European capitals (in any order).
2. Print the cities on separate lines.
3. Sort the list alphabetically.
4. Allow the user to add two new European capitals and sort the list again.
5. Display the city names in alphabetical order, adding a sequence number before each name.
6. Add a summary sentence to the output: "Our list contains 12 European capitals",
where the number of cities is obtained using an appropriate function.
"""


capitals = ["Tallinn", "Riia", "Pariis",
            "Helsinki", "Vilnus", "Sofia",
            "Tirana", "Oslo", "Stockholm", "Belgrad"]

def print_list (elements: list) -> None:
    for element in elements:
        print(element, end=", ")
    print()

def sort_in_place (elements: list) -> None:
    elements.sort()


def add_capitols(capitols: list, amount: int)-> None:
    for i in range(amount):
        capitols.append(input(f"{i + 1}. Sisesta Euroopa pealinn: ").strip())


def print_list_numbered (elements: list) -> None:
    for index, element in enumerate(elements):
        print(f"{index + 1}.{element}")
    print()


def summarize(capitals: list[str]) -> None:
    print(f"Meie järjendis on {len(capitals)} Euroopa pealinna")

if __name__ == '__main__':
    print_list(capitals)
    sort_in_place(capitals)
    print_list(capitals)
    add_capitols(capitals, 2)
    sort_in_place(capitals)
    print_list(capitals)
    print_list_numbered(capitals)
    summarize(capitals)