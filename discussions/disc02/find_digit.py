def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    def f(n):
        i = 0
        while i < k:
            digit, n = n % 10, n // 10
            i += 1
        return digit
    return f
