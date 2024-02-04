# What is the value of result after executing
# result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)?

# 1)    Rewrite everything as normal functions, not lambdas.

def f(x):
    def g(y):
        return 3
    return 2 * g(4) * x

# 2)    Evaluate the function call f(5)

#       This means evaluating 2 * g(4) * 5, which is equal to 10 * g(4).
#       The function g always returns 3, no matter what it is passed as an
#       argument.
#       Therefore f(5) returns 10 * 3 which is 30.

my_result = f(5)
result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)

assert my_result == 30
assert my_result == result
