from operator import add, mul

def square(x):
    return mul(x, x)

def sum_squares(x, y):
    # return square(x) + square(y)
    return add(square(x), square(y))

################################################################################

if __name__ == "__main__":
    print("square(2) -> ", square(2))
    print("square(-5) -> ", square(-5))
    print("sum_squares(3, 4) -> ", sum_squares(3, 4))
