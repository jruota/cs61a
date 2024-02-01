def compose1(f, g):
    return lambda x: f(g(x))


################################################################################

if __name__ == "__main__":
    s = lambda x: x * x
    print(s(12))
