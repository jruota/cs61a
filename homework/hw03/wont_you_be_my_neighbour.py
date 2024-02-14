def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(0)
    0
    >>> repeat_digits(1)
    11
    >>> repeat_digits(12)
    1122
    >>> repeat_digits(123)
    112233
    >>> repeat_digits(12340)
    1122334400
    >>> repeat_digits(1234)
    11223344
    """

    # if n < 10:
    #     return 10 * n + n
    # else:
    #     last, rest = n % 10, n // 10
    #     return repeat_digits(rest) * 100 + (10 * last + last)

    last, rest = n % 10, n // 10
    if rest == 0:
        return last * 10 + last
    return repeat_digits(rest) * 100 + (last * 10 + last)
