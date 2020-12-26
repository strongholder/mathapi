import functools
import math


@functools.lru_cache(1000)
def factorial(n):
    return math.factorial(n)
