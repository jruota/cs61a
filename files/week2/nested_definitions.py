from functions_as_general_methods import approx_eq, improve


def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)


def average(x, y):
    return (x + y)/2


def sqrt_test():
    assert sqrt(0) == 0         # fails
    assert sqrt(1/9) == 1/3
    assert sqrt(1/2) == 1/4
    assert sqrt(1) == 1
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(16) == 4


################################################################################

if __name__ == "__main__":
    sqrt_test()
