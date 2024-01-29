# two calls to function f
def print_then_return_v1(x):
    print(f(x))
    return f(x)

# one call to function f
def print_then_return_v2(x):
    y = f(x)
    print(y)
    return

# What is a function f for which implementations v1 and v2 would have different
# behavior?
def f(x):
    print(x)

################################################################################

if __name__ == "__main__":
    print("Running implementation v1.")
    print_then_return_v1(2)
    # print(print_then_return_v1(2))
    print("Running implementation v2.")
    print_then_return_v2(2)
    # print(print_then_return_v2(2))
