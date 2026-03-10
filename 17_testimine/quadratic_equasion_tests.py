import pytest
from quadric_equasion import solve_quadratic_equation as solve

def test_normal_values():
    assert solve(1, -3, 2) == (1, 2)


def test_float_values():
    assert solve(1, -4, 3.75) == (1.5, 2.5)


def test_one_solution():
    assert solve(1, -4, 4) == (2, )