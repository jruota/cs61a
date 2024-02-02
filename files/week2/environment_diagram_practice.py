def f(x):
    """f(x)(t) returns max(x*x, 3*x) if t(x) > 0, and 0 otherwise."""

    y = max(x * x, 3 * x)
    def zero(t):
        if t(x) > 0:
            return y
        return 0
    return zero


# Find the largest positive y below 10 for which f(y)(lambda z: z - y + 10) is
# not 0.
y = 1
while y < 10:
    if f(y)(lambda z: z - y + 10):
        max = y
    y = y + 1
