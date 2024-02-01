def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique_digit_count = 0
    i = 0
    while i <= 9:
        unique_digit_count += has_digit(n, i)
        i += 1
    return unique_digit_count


def has_digit(n, k):
    """Returns whether k is a digit in n.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n > 0:
        digit = n % 10
        n //= 10
        if digit == k:
            return True
    return False
