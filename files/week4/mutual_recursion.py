"""When a recursive procedure is divided among two functions that call each
other, the functions are said to be mutually recursive. As an example, consider
the following definition of even and odd for non-negative integers:

    - a number is even if it is one or more than an odd number
    - a number is odd if it is one more than an even number
    - 0 is even
"""


def is_even(n):
    """Is n even?

    n - positive integer (including zero)

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    >>> is_even(6)
    True
    >>> is_even(7)
    False
    >>> is_even(8)
    True
    >>> is_even(9)
    False
    >>> is_even(10)
    True
    >>> is_even(472)
    True
    >>> is_even(473)
    False
    """
    if (n == 0):
        return True
    return is_odd(n - 1)


def is_odd(n):
    """Is n odd?

    n - positive integer (including zero)

    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(2)
    False
    >>> is_odd(3)
    True
    >>> is_odd(4)
    False
    >>> is_odd(5)
    True
    >>> is_odd(6)
    False
    >>> is_odd(7)
    True
    >>> is_odd(8)
    False
    >>> is_odd(9)
    True
    >>> is_odd(10)
    False
    >>> is_odd(472)
    False
    >>> is_odd(473)
    True
    """
    if (n == 0):
        return False
    return is_even(n - 1)


def is_even_v2(n):
    """Is n even?

    n - positive integer (including zero)

    >>> is_even_v2(0)
    True
    >>> is_even_v2(1)
    False
    >>> is_even_v2(2)
    True
    >>> is_even_v2(3)
    False
    >>> is_even_v2(4)
    True
    >>> is_even_v2(5)
    False
    >>> is_even_v2(6)
    True
    >>> is_even_v2(7)
    False
    >>> is_even_v2(8)
    True
    >>> is_even_v2(9)
    False
    >>> is_even_v2(10)
    True
    >>> is_even_v2(472)
    True
    >>> is_even_v2(473)
    False
    """
    if (n == 0):
        return True
    else:
        if ((n - 1) == 0):
            return False
        return is_even_v2(n - 2)


def is_odd_v2(n):
    """Is n odd?

    n - positive integer (including zero)

    >>> is_odd_v2(0)
    False
    >>> is_odd_v2(1)
    True
    >>> is_odd_v2(2)
    False
    >>> is_odd_v2(3)
    True
    >>> is_odd_v2(4)
    False
    >>> is_odd_v2(5)
    True
    >>> is_odd_v2(6)
    False
    >>> is_odd_v2(7)
    True
    >>> is_odd_v2(8)
    False
    >>> is_odd_v2(9)
    True
    >>> is_odd_v2(10)
    False
    >>> is_odd_v2(472)
    False
    >>> is_odd_v2(473)
    True
    """
    if (n == 0):
        return False
    else:
        if ((n -1) == 0):
            return True
        return is_odd_v2(n - 2)
