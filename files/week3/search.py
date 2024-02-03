def search(f):
    """Return f(x) for the integers x >= 0 until f(x) returns a value other
    than 0.
    """
    x = 0
    while (not f(x)):
        x += 1
    return x


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    # Negative values are truthy, so to make sure that no x for which
    # square(x)-100 is negative is returned, max(0, square(x) - 100) is used.
    return max(0, square(x) - 100)


def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)
    # The inner lambda (lambda x: f(x) == y) return either True or False.
    # Passing it to search returns the first x for which this lambda function
    # returns True [under the assumption that x is a positive integer, i.e. a
    # perfect square].


################################################################################


print(search(is_three))
print(search(positive))

print()

sqrt = inverse(square)
print(square(16))
print(sqrt(square(16)))
