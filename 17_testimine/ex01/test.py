"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(1, True) is False


def test__students_study__morning_without_coffee__no_studying():
    """During morning without coffee students do not study."""
    assert students_study(7, False) is False


def test__students_study__evening_with_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(18, True) is True


def test__students_study__morning_with_coffee__studying():
    """During morning with coffee students study."""
    assert students_study(17, True) is True


#student_study__night_coffee_false
def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(4, False) is False


#student_study__evening_coffee_false
def test__students_study__evening_without_coffee__studying():
    """During evening with coffee students study."""
    assert students_study(24, False) is True

#student_study__evening_edge_case_coffee_true
#student_study__evening_edge_case_coffee_false
#student_study__night_edge_case_coffee_true
#student_study__night_edge_case_coffee_false
#
#student_study__day_edge_case_coffee_true
#student_study__day_edge_case_coffee_false

def test__lottery_all_numbers_equal_5():
    """Lottery numbers 5, 5, 5 give win 10."""
    assert lottery(5, 5, 5) == 10


def test__lottery_all_numbers_equal_and_positive_but_not_5():
    """Lottery numbers 3, 3, 3 give win 5."""
    assert lottery(3, 3, 3) == 5


# lottery__all_same_negative
def test__lottery_all_numbers_equal_and_negative():
    """Lottery numbers -3, -3, -3 give win -1."""
    assert lottery(-3, -3, -3) == -1


# lottery__all_same_zero
def test__lottery_all_numbers_equal_zero():
    """Lottery numbers 0, 0, 0 give win -1."""
    assert lottery(0, 0, 0) == -1


def test__lottery_both_numbers_different_from_first_number():
    """Lottery numbers 1, 3, 3 give win 1."""
    assert lottery(1, 3, 3) == 1


def test__lottery_one_of_numbers_equal_with_first_number():
    """Lottery numbers 1, 3, 1 give win 0."""
    assert lottery(1, 3, 1) == 0


# lottery__a_b_same_c_diff
def test__lottery_two_first_numbers_equal_third_is_different_but_not_five():
    """Lottery numbers 1, 1, 3 give win 5."""
    assert lottery(1, 1, 3) == 5


def test__lottery_two_first_numbers_equal_third_equals_five():
    """Lottery numbers 2, 2, 5 give win -1."""
    assert lottery(2, 2, 5) == -1

# lottery__all_diff
def test__lottery_all_numbers_are_different():
    """Lottery numbers 1, 2, 3 give win -1."""
    assert lottery(1, 2, 3) == -1

def test__fruit_order_only_small_baskets_used_without_leftovers():
    """4 small baskets, 3 big baskets, 4 kg fruits order -> 4."""
    assert fruit_order(4, 3, 4) == 4


def test__fruit_order_only_big_baskets_used_without_leftovers():
    """4 small baskets, 3 big baskets, 15 kg fruits order -> 0."""
    assert fruit_order(4, 3, 15) == 0


def test__fruit_order_both_type_of_baskets_used_with_leftovers():
    """2 small baskets, 1 big baskets, 8 kg fruits order -> -1."""
    assert fruit_order(2, 1, 8) == -1


def test__fruit_order_both_type_of_baskets_used_without_leftovers():
    """3 small baskets, 1 big baskets, 8 kg fruits order -> 3."""
    assert fruit_order(3, 1, 8) == 3


#fruit_order__all_zero
def test__fruit_order_all_data_is_zero():
    """0 small baskets, 0 big baskets, 0 kg fruits order -> 0."""
    assert fruit_order(0, 0, 0) == 0


#fruit_order__zero_amount_zero_small
def test__fruit_order_amount_and_small_baskets_are_zero():
    """0 small baskets, 3 big baskets, 0 kg fruits order -> 0."""
    assert fruit_order(3, 0, 0) == 0


#fruit_order__zero_amount_zero_big

#fruit_order__zero_amount_others_not_zero
#fruit_order__only_big_exact_match
#fruit_order__only_big_not_enough_but_multiple_of_5
#fruit_order__only_big_not_enough
#fruit_order__only_big_more_than_required_match
#fruit_order__only_big_more_than_required_no_match
#fruit_order__only_small_match_more_than_5_smalls
#fruit_order__only_small_not_enough_more_than_5_smalls
#fruit_order__only_small_exact_match
#fruit_order__only_small_not_enough
#fruit_order__only_small_more_than_required
#fruit_order__match_with_more_than_5_smalls
#fruit_order__use_some_smalls_some_bigs
#fruit_order__enough_bigs_not_enough_smalls
#fruit_order__not_enough_with_more_than_5_smalls
#fruit_order__enough_bigs_not_enough_smalls_large_numbers
#fruit_order__match_large_numbers