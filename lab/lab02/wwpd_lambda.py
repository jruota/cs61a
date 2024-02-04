print(lambda x: x)
# Function

a = lambda x: x
print(a(5))
# 5

print((lambda: 3)())
# 3

b = lambda x, y: lambda: x + y
c = b(8, 4)
print(c)
# Function

print(c())
# 12

d = lambda f: f(4)
def square(x):
    return x * x
print(d(square))
# 16


higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
# higher_order_lambda(2)(g)
# Error - int is not callable

print(higher_order_lambda(g)(2))
# 4

call_thrice = lambda f: lambda x: (f(f(f(x))))
print(call_thrice(lambda y: y + 1)(0))
# 3

print_lambda = lambda z: print(z)
# When is the return expression of a lambda expression executed?
#   It returns after the print has printed, and the return value is None.
print(print_lambda)
# Function

one_thousand = print_lambda(1000)
# 1000 (is being printed by print_lambda)

print(one_thousand)
# None
