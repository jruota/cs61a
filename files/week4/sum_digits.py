def sum_digits_recursive(n):
    """Return the sum of the digits of positive integer n.

    >>> sum_digits_recursive(9)
    9
    >>> sum_digits_recursive(18117)
    18
    >>> sum_digits_recursive(9437184)
    36
    >>> sum_digits_recursive(11408855402054064613470328848384)
    126
    """
    if (n < 10):
        return n
    last_digit, rest = (n % 10), (n // 10)
    return sum_digits_recursive(rest) + last_digit


def sum_digits_iterative(n):
    """Return the sum of the digits of positive integer n.

    >>> sum_digits_iterative(9)
    9
    >>> sum_digits_iterative(18117)
    18
    >>> sum_digits_iterative(9437184)
    36
    >>> sum_digits_iterative(11408855402054064613470328848384)
    126
    """
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += (n % 10)
        n //= 10
    return sum_of_digits
