def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    >>> swipe(8)
    8
    >>> swipe(23)
    3
    2
    3
    """
    if n < 10:
        print(n)
    else:
        all_but_last, last = n // 10, n % 10
        print(last)
        swipe(all_but_last)
        print(last)
