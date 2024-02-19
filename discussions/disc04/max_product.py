def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1

    >>> max_product([1, 2, 3, 4])
    8
    >>> max_product([1, 2, 3])
    3
    >>> max_product([1, 2])
    2
    >>> max_product([23])
    23
    """
    if len(s) < 1:
        return 1
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))
