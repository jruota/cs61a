def cascade(n):
    """Print a cascade of prefixes of n.

    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    """
    if (n < 10):
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


################################################################################


if __name__ == "__main__":
    cascade(1234567890)
