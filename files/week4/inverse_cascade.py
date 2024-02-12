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

    def upper_cascade(n0):
        if n0 < 10:
            print(n0)
        else:
            upper_cascade(n0 // 10)
            print(n0)

    def lower_cascade(n0):
        if n0 >= 10:
            print(n0)
            lower_cascade(n0 // 10)
        else:
            print(n0)

    if n < 10:
        print(n)
    else:
        upper_cascade(n // 10)
        print(n)
        lower_cascade(n // 10)


if __name__ == "__main__":
    inverse_cascade(0)
    print()
    inverse_cascade(1)
    print()
    inverse_cascade(2)
    print()
    inverse_cascade(3)
    print()
    inverse_cascade(4)
    print()
    inverse_cascade(5)
    print()
    inverse_cascade(6)
    print()
    inverse_cascade(7)
    print()
    inverse_cascade(8)
    print()
    inverse_cascade(9)
    print()
    inverse_cascade(10)
    print()
