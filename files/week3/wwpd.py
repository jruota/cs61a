from operator import add, mul


def square(x):
    return mul(x, x)


def delay(arg):
    print("delayed")
    def g():
        return arg
    return g


def pirate(arggg):
    print("matey")
    def plunder(arggg):
        return arggg
    return plunder


################################################################################


delay(delay)()(6)()

"""
1)  Evaluate the operator expression delay(delay)

        - prints "delayed"
        - defines g
        - returns g

2)  Call g with no arguments, i.e. g()

        - returns arg, which is found in the parent environment
        - arg evaluates to the function delay

3)  Call delay(6)

        - prints "delayed"
        - defines g
        - returns g

4)  Call g()

        - returns arg, which is found in the parent environment
        - arg evaluates to the value 6

So the interactive session would look like this:

>>> delay(delay)()(6)()
delayed
delayed
6
"""


################################################################################


print(delay(print)()(4))

"""
Work from the inside out.

1)  Evaluate delay(print)

        - prints "delayed"
        - defines g
        - returns g

2)  Evaluate g()

        - returns arg, which is found in the parent environment
        - arg evaluates to the function print


3)  Evaluate print(4)

        - prints 4
        - return None

4)  Evaluate print(None)

        - prints None

The interactive session would look like this:

>>> print(delay(print)()(4))
delayed
4
None
"""


################################################################################


add(pirate(3)(square)(4), 1)

"""
1)  Evaluate pirate(3)

        - prints "matey"
        - defines plunder
        - returns plunder

2)  Evaluate plunder(square)

        - plunder returns its argument, which is the function square

3)  Evaluate square(4)

        - returns 16

4)  Evaluate add(16, 1)

        - returns 17

The interactive session would look like this:

>>> add(pirate(3)(square)(4), 1)
matey
17
"""


################################################################################


pirate(pirate(pirate))(5)(7)

"""
1)  Evaluate pirate(pirate)

        - prints "matey"
        - returns plunder

2)  Evaluate pirate(plunder)

        - prints "matey"
        - returns plunder

3)  Evaluate plunder(5)

        - returns 5

4)  Evaluate 5(7)

        - throws an error, int object not callable

The interactive session would look like this:

>>> pirate(pirate(pirate))(5)(7)
matey
matey
ERROR
"""
