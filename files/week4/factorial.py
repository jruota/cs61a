def factorial_recursive(n):
    """Return the factorial of natural number n.

    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(2)
    2
    >>> factorial_recursive(3)
    6
    >>> factorial_recursive(4)
    24
    >>> factorial_recursive(20)
    2432902008176640000
    """
    # The base case could also be simplified to only testing the case where
    # n == 0.
    if (n == 0 or n == 1):
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Return the factorial of natural number n.

    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(1)
    1
    >>> factorial_iterative(2)
    2
    >>> factorial_iterative(3)
    6
    >>> factorial_iterative(4)
    24
    >>> factorial_iterative(20)
    2432902008176640000
    """
    factorial, i = 1, 2
    while (i <= n):
        factorial *= i
        i += 1
    return factorial
