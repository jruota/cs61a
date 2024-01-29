from math import floor

def nice(n):
    """Return n if it is a nice number or round n to make it nice.

    Definition of a nice number:
        A nice number doesn't have 98, 99, 01, or 02 among its digits and 00 can
        only be followed by more 0's.

    n -- integer >= 0

    >>> nice(0)         # already nice
    0
    >>> nice(1)         # already nice
    1
    >>> nice(10)        # already nice
    10
    >>> nice(97)        # already nice
    97
    >>> nice(98)        # 98
    100
    >>> nice(99)        # 99
    100
    >>> nice(2799)      # 99
    2800
    >>> nice(5016)      # 01
    5000
    >>> nice(9902)      # 02 AND 99
    10000
    >>> nice(1200456)   # 00 followed by non-zero digits
    1200000
    >>> nice(98402001)  # 02 OR 00 followed by non-zero digits
    100000000
    >>> nice(755)       # already nice
    755
    >>> nice(2859)      # already nice
    2859
    >>> nice(45622895)  # already nice
    45622895
    """
    def change_n(n0, n2d):
        if (n2d == 99 or n2d == 98 or n2d < 3):
            n0 = round(n0 / pow(base, exp)) * pow(base, exp)
        return n0

    if (n < 98):
        return n

    base = 10
    exp = 2
    # Look for 98 or 99 or 01 or 02 among the digits.
    while ((n / pow(base, exp)) > 0.1):
        rest = n % pow(base, exp)
        next2digits = floor(rest / (pow(base, exp-2)))
        n = change_n(n, next2digits)
        exp += 1

    return n

################################################################################

if __name__ == "__main__":
    print(nice(5016))
    print(nice(9902))
    print(nice(1200456))
    print(nice(98402001))
