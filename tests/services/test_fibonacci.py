import random

from mathapi.services.fibonacci import InvalidInputError, nth_fibonacci


def test_negative():
    try:
        nth_fibonacci(-1)
        raise AssertionError("The number must be a non-negative integer")
    except InvalidInputError:
        pass


def test_zero_fibonacci():
    assert nth_fibonacci(0) == 0


def test_first_fibonacci():
    assert nth_fibonacci(1) == 1


def test_second_fibonacci():
    assert nth_fibonacci(2) == 1


def test_third_fibonacci():
    assert nth_fibonacci(3) == 2


def test_random_fibonacci():
    for n in (random.randint(1, 100000) for _ in range(20)):
        print(f"fib({n}) = {nth_fibonacci(n)}")
        assert nth_fibonacci(n) == nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
