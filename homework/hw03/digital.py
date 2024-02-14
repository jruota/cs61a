def collapse(n):
    """For non-negative N, the result of removing all digits that are equal to
    the digit on their right, so that no adjacent digits are the same.

    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """

    left, last = n // 10, n % 10
    if left <= 0:
        return last
    elif last == (left % 10):
        return collapse(left)
    else:
        return collapse(left) * 10 + last


def find_pair(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair(lambda a, b: a == b) # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> z(123412)
    True
    >>> find_pair(lambda a, b: a <= b)(9753)
    False
    >>> find_pair(lambda a, b: a == 1)(1) # Only one digit; no pairs.
    False
    """

    # def find(n):
    #     while n >= 10:
    #         if p((n // 10) % 10, n % 10):
    #             return True
    #         else:
    #             n //= 10
    #     return False
    # return find

    def find(n):
        if n < 10:
            return False
        else:
            return p((n // 10) % 10, n % 10) or find(n // 10)
    return find
