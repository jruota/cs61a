import sys
sys.path.insert(0, "../../tools/")
from tracer import tracer


def pal(n):
    """Return a palindrom starting with n.

    >>> pal(12430)
    1243003421
    """
    m = n
    while m:
        n, m = n * 10 + m % 10, m // 10
    return n


def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.

    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if (a % 10) == (b % 10):
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)


def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.
    >>> biggest_palindrome(3425534)
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    return big(n, 0)

@tracer
def big(n, k):
    """A helper function for biggest_palindrome."""
    if n == 0:
        return 0
    choices = [big(n // 10, k), big(n // 10, 10 * k + n % 10)]
    if (contains(k, n)):
        choices.append(pal(k))
    return max(choices)


################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
################################################################################


if __name__ == "__main__":
    # big(3425534, 0)
    # big(45534, 0)
    big(4554, 0)
