def is_prime(n):
    """Returns True if n is a prim number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def is_prime_helper(i):
        """"""
        if i >= n:
            return True
        else:
            return is_prime_helper(i + 1) and (n % i != 0)

    return is_prime_helper(2)
