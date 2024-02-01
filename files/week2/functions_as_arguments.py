def sum_naturals(n):
    """Compute the sum of natural numbers up to n inclusive.

    n -- upper bound of the sum, integer >= 0

    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    """Compute the sum of the cubes of natural numbers up to n inclusive.

    n -- upper bound of the sum, integer >= 0

    >>> sum_cubes(100)
    25502500
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total


def pi_sum(n):
    """Compute the sum of the first n terms of a series that slowly converges
    to pi.

    n -- upper bound of the sum, integer >= 0

    >>> pi_sum(100)
    3.1365926848388144
    """
#    total, k = 0, 0
#    while k < n:
#        l = 1 + k * 4
#        total += 8 / (l * (l + 2))
#        k += 1
#    return total
    total, k = 0, 1
    while k <= n:
        total, k = total + (8 / ((4*k-3) * (4*k-1))), k + 1
    return total


def summation(n, term):
    """Abstraction of summation functions.

    n -- upper bound of the sum, integer >= 0
    term -- function that computes the kth term
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def summation_test():
    assert summation(100, identity) == sum_naturals(100)
    assert summation(100, cube) == sum_cubes(100)
    assert summation(100, pi_term) == pi_sum(100)


def identity(x):
    return x


def cube(x):
    return pow(x, 3)


def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))


################################################################################

if __name__ == "__main__":
    summation_test()
