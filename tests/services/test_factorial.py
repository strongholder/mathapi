import random

from mathapi.services.factorial import InvalidInputError, factorial


def test_zero_n():
    assert factorial(0) == 1


def test_negative_n():
    try:
        factorial(-42)
        raise AssertionError("factorial not defined for negative values")
    except InvalidInputError:
        pass


def test_positive_n():
    for n in (random.randint(1, 10000) for _ in range(20)):
        assert factorial(n) / factorial(n - 1) == n
