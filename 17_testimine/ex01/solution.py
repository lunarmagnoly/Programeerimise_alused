"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time in range(18, 25):
        return True
    elif time in range(5, 18) and coffee_needed:
        return True
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c != 5:
        return 5
    elif b != a and c != a:
        return 1
    elif b == a or c == a:
        return 0
    return -1


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    big_basket_capacity = 5
    small_basket_capacity = 1

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1

    """
    max_big_baskets_amount = ordered_amount // 5
    used_big_baskets = min(max_big_baskets_amount, big_baskets)
    left = ordered_amount - (used_big_baskets * 5)
    if small_baskets >= left:
        return left
    else:
        return -1