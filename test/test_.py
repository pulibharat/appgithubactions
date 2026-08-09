from re import sub

from src.maths_operation import sum, subtract


def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(10, 1) == 11


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, 5) == 0
    assert subtract(10, -11) == 21
