import functools


@functools.lru_cache(1000)
def power(base, exponent):
    return base ** exponent
