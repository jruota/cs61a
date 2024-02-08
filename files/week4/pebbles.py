def play_alice(n):
    if (n == 0):
        print("Bob wins!")
    else:
        print("Alice takes one pebble. There are", n - 1, "pebbles now.")
        play_bob(n - 1)


def play_bob(n):
    if (n == 0):
        print("Alice wins!")
    else:
        if (n % 2 == 0):
            take = 2
        else:
            take = 1
        print("Bob takes",
              take,
              "pebbles. There are",
              n - take,
              "pebbles now.")
        play_alice(n - take)
