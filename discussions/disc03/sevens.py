def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        else:
            if has_seven(i) or i % 7 == 0:
                direction *= -1
            i += 1
            who = ((who + direction) % 5)
            if who == 0:
                who = 5
            # print("DEBUG: i", i)
            # print("DEBUG: who", who)
            # print("DEBUG: direction", direction)
            return f(i, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


if __name__ == "__main__":
    sevens(9, 5)
