def fib(n):
    """Return the nth fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(7)
    13
    >>> fib(18)
    2584
    >>> fib(36)
    14930352
    >>> fib(41)
    165580141
    """
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib(n - 1) + fib(n - 2)
