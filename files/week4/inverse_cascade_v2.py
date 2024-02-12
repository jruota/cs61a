def inverse_cascade(n):
    """
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1

    >>> inverse_cascade(1234567890)
    1
    12
    123
    1234
    12345
    123456
    1234567
    12345678
    123456789
    1234567890
    123456789
    12345678
    1234567
    123456
    12345
    1234
    123
    12
    1
    """

    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)
def grow(n):
    if n // 10:
        grow(n // 10)
        print(n // 10)


shrink = lambda n: f_then_g(print, shrink, n // 10)
def shrink(n):
    if n // 10:
        print(n // 10)
        shrink(n // 10)
