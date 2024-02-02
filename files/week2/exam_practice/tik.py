def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.

    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        print(tok, gram)
    return insta


################################################################################

# What would the interactive Python interpreter display upon evaluating the
# expression tik(tik(5)(print(6)))(print(7))

# 6
# 5 None
# 7
# None None

tik(tik(5)(print(6)))(print(7))
