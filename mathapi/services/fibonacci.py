def nth_fibonacci(n):
    """
    see: https://stackoverflow.com/a/23462371
    """

    v1, v2, v3 = 1, 1, 0

    # perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1 = v1 * v1 + calc
        v2 = (v1 + v3) * v2
        v3 = calc + v3 * v3

        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2

    return v2
