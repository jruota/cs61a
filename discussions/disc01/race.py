def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.
    >>> race(5, 7) # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


################################################################################


# Find positive integers x and y (with y larger than x but not larger than 2*x)
# for which either:
#       - race(x, y) returns the wrong value or
#       - race(x, y) runs forever

print(race(2, 3))

# When called with x=2 and y=3 print returns 15, but the tortoise will have
# passed the hare for the first time after 7.5 minutes.
# But the function only works with integers and 7.5 is not. Therefore the
# function only returns for multiples of 7.5 that are integers, the first being
# 15.

race(4, 5)  # RUNS FOREVER!!!

# In the first 5 minutes the tortoise is trailing the hare, but overtakes the
# the hare after 6.25 minutes. This is not caught by the function, because it
# is not an integer. After that the tortoise leads and the hare never catches
# up -> the function runs forever.
