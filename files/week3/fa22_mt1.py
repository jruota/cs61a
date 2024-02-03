print((3 and 4) - 5)    # -1


################################################################################


# WRONG
# Applies a function to itself, multiplication is not defined for functions.
def funsquareA(f):
    return f(f)

# WRONG
# Returns a function that takes no arguments, should take one argument.
def funsquareB(f):
    return lambda: f(f)


# WRONG
# Takes a second argument that is not used.
# Would work if one would supply a second argument that is ignored.
def funsquareC(f, x):
    def g(x):
        return f(f(x))
    return g


# CORRECT
def funsquareD(f):
    return lambda x: f(f(x))


# WRONG
# As in C, takes a second argument that is not used.
# Does not return a one-argument function, but the value of
# the expression f(f(x)).
def funsquareE(f, x):
    return f(f(x))


# CORRECT
def funsquareF(f):
    def g(x):
        return f(f(x))
    return g


triple = lambda x: 3 * x
print(funsquareF(triple)(5))    # Equivalent to triple(triple(5))


################################################################################


snap = lambda chat: lambda: snap(chat)
snap, chat = print, snap(2020)
# What is diplayed here? -> NOTHING
chat()
# What is displayed here? -> 2020

# STEPS TO SOLVE THIS
# 1) Rewrite the first assignment to snap as a regular function.
#
#       def g(chat):
#           def h():
#               return snap(chat)
#       return h
#
#       snap = g
#
# 2) Evaluate snap(2020)
#
#       snap(2020) = g(2020) = h
#       [the formal parameter chat is bound to the integer 2020 in the enclosing
#        scope]
#
# 3) Make the assignments. They do not print anything.
#
#       snap is an alias for the print function.
#       chat is the return value of snap(2020), that is the no-argument h.
#
# 4) Evaluate the function call.
#
#       chat() = h() -> print the value the formal parameter chat of function g
#                       from step 1 is bound to, which is the integer 2020
