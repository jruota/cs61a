assert (True and 13) == 13
assert (False or 0) == 0
assert (not 10) == False
assert (not None) == True

# True and 1 / 0  # Error [ZeroDivision]
assert (True or 1 / 0) == True
assert (-1 and 1 > 0) == True
assert (-1 or 5) == -1
assert ((1 + 1) and 1) == 1
assert (print(3) or "") == ""


def f(x):
    if x == 0:
        return "zero"
    elif x > 0:
        return "positive"
    else:
        return ""


assert (0 or f(1)) == "positive"
assert (f(0) or f(-1)) == "zero"
assert (f(0) and f(-1)) == ""
