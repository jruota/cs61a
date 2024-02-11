i = 1
n = 8

def main_iterative():
    i, j = 1, 0
    while i <= n:
        i += 1
        if i % 2 == 0:
            j += 1
    print(j)


def main():
    global i        # i is the starting x-coordinate of Karel
    if i < n:       # equivalent to front_is_clear()
        i += 1      # equivalent to move()
        if i < n:
            i += 1
            main()
    else:
        pass        # equivalent to calling turn_left twice
    if i > 1:       # equivalent to front_is_clear() after turning twice
        i -= 1


################################################################################


# main_iterative()
if __name__ == "__main__":
    for j in range(1, 15):
        i = 1
        n = j
        print("Karel starts at position", i)
        print("The canvas is", n, "units big")
        main()
        print("Karel's final position is", i)
        assert i == n // 2 or i == n // 2 + 1
        print()
