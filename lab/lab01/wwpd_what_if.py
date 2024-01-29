def ab(c, d):
    """
    >>> ab(10, 20)
    10
    foo
    """
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print("foo")

def bake(cake, make):
    """
    >>> bake(0, 29)
    1
    29
    29
    >>> bake(1, "mashed potatoes")
    mashed potatoes
    'mashed potatoes'
    """
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
