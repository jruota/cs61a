def is_prime(n):
    """Return True if n is a prime number and False otherwise.

    For the history of 1 as a prime / non-prime number see
    https://blogs.scientificamerican.com/roots-of-unity/why-isnt-1-a-prime-number/

    n -- positive integer >= 1

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if (n == 1):
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
