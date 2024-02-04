def remove(n, digit):
    """Return all digits of non-negative N that are not DIGIT, for some
    non-negative DIGIT less than 10.

    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    power, res = 0, 0
    while n > 0:
        next_digit, n = n % 10, n // 10
        if (next_digit != digit):
            res += next_digit * pow(10, power)
            power += 1
    return res


# This next version was written to match the template from the lecture videos.
def remove_v2(n, digit):
    """Return all digits of non-negative N that are not DIGIT, for some
    non-negative DIGIT less than 10.

    >>> remove_v2(231, 3)
    21
    >>> remove_v2(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * pow(10, digits)
            digits = digits + 1
    return kept
