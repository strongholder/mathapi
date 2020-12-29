import math

from mathapi.services.exponent import power


def test_positive_exponents():
    positive_numbers = [1, 2, 3, 5, 7, 100000]

    for b in positive_numbers:
        for n in positive_numbers:
            # 1st power
            assert power(b, 1) == b

            # recurrence relation
            assert power(b, n + 1) == power(b, n) * b


def test_zero_exponent():
    for b in [-2e42, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 2e42]:
        assert power(b, 0) == 1


def test_negative_exponent():
    for b in [-7, -5, -3, -2, -1, 1, 2, 3, 5, 7, 100000]:
        for e in [-100000, -7, -5, -3, -2, -1]:
            assert power(b, e) == 1 / power(b, -e)

    try:
        0 ** -1
        raise AssertionError("0.0 cannot be raised to a negative power")
    except Exception:
        pass


def test_rational_exponents():
    numbers = [1, 3, 5, 7, 9, 99999]

    for b in numbers:
        assert power(b, 0.5) == math.sqrt(b)


def test_properties():
    numbers = [1, 3, 5, 7, 9]

    for b in numbers:
        for n in numbers:
            for m in numbers:
                assert power(b, m + n) == power(b, m) * power(b, n)
                assert power(power(b, m), n) == power(b, m * n)
                assert power(b * m, n) == power(b, n) * power(m, n)
