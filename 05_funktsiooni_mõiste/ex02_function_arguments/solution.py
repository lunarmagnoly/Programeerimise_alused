"""Function examples."""


def func():
    """Print: I´m inside the function."""
    print("I´m inside the function")


def my_name_is(name: str):
    """Print: My name is [name]."""
    print(f"My name is {name}")


def sum_six(num: int) -> int:
    """Return sum of num and 6."""
    return num + 6


def sum_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def usd_to_eur(amount: int):
    """Return USD in EUR if 1 USD = 0.8 EUR."""
    return amount * 0.8


if __name__ == '__main__':
    func()
    my_name_is("Mari")
    sum_six_result = sum_six(5)
    assert sum_six_result == 11
    sum_numbers_result = sum_numbers(3, 5)
    assert sum_numbers_result == 8
    usd_to_eur_result = usd_to_eur(300)
    assert usd_to_eur_result == 240