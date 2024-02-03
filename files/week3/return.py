def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5

    >>> end(12346789, 5)
    9
    8
    7
    6
    4
    3
    2
    1
    """

    # Using n_copy instead of n so that a reference to the original number
    # remains. If that is of no use, one could use n directly instead of n_copy.
#    next_digit = n % 10
#    n_copy = n
#    while (n_copy > 0):
#        print(next_digit)
#        if (next_digit == d):
#            return
#        n_copy //= 10
#        next_digit = n_copy % 10

    while (n > 0):
        digit, n = n % 10, n // 10
        print(digit)
        if (digit == d):
            return
