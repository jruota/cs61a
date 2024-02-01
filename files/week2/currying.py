def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1


def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f


################################################################################

if __name__ == "__main__":
    print(curried_pow(2)(3))
    map_to_range(0, 10, curried_pow(2))

    print()

    pow_curried = curry2(pow)
    print(pow_curried(2)(5))
    map_to_range(0, 10, pow_curried(2))
    print(uncurry2(pow_curried)(2, 5))
