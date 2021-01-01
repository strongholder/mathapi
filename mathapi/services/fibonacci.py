import functools


class InvalidInputError(Exception):
    pass


@functools.lru_cache(1000)
def nth_fibonacci(n):
    """
    see: https://stackoverflow.com/a/23462371
    """
    if n < 0:
        raise InvalidInputError("The number must be a non-negative integer")

    if n == 0:
        return 0

    v1, v2, v3 = 1, 1, 0

    # perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return v2
