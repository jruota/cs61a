from random import randint


def dice():
    """A dice function returns an integer that is the outcome
    of rolling once.
    """

    return randint(1, 6)


# Implement repeats, which returns the # of times in n rolls that repeat the
# last roll.
def repeats(n, dice):
    count = 0
    previous = 0
    while n > 0:
        roll = dice()
        print("DEBUG: ", roll)
        if roll == previous:
            count += 1
        previous = roll
        n -= 1
    return count


################################################################################


print(repeats(20, dice))
