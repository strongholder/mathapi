import functools


class ZeroDivisionError(Exception):
    pass


@functools.lru_cache(1000)
def power(base, exponent):
    """
    Compute base^exponent power
    """
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative number")

    return base ** exponent
