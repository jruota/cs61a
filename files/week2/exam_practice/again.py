def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)


def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)


def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for
    some m < n.

    >>> again(parabola)     # parabola(4) == parabola(5)
    5
    >>> again(vee)          # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(n) == f(m):
                return n
            m += 1
        n = n + 1
