import functools
import math


class InvalidInputError(Exception):
    pass


@functools.lru_cache(1000)
def factorial(n):
    if n < 0:
        raise InvalidInputError("Factorial not defined for negative values")

    return math.factorial(n)
