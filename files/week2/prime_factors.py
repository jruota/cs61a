def prime_factors(n):
    """Return a list of the prime factors of n.

    n -- positive integer >= 2

    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(9)
    [3, 3]
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(858)
    [2, 3, 11, 13]
    """
    factor_list = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            factor_list.append(factor)
            n //= factor
        else:
            factor += 1
    return factor_list
