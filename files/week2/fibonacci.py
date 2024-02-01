"""Discussion question:
    Is this alternative definition of fib (fib2) the same or different from the
    original fib (fib1)?

    Except for the fact that fib2 can compute the 0th Fibonacci number, these
    two functions are equivalent. But the order of pred and curr changes in fib2
    when k switches from 0 to 1, which can be confusing.

    fib2(5)
    pred    curr    k   n   k<n
    1       0       0   5   t
    0       1       1   5   t
    1       1       2   5   t
    1       2       3   5   t
    2       3       4   5   t
    3       5       5   5   f

Link to the video:
    https://youtu.be/pveIuZT0GJE?list=PL6BsET-8jgYXvcnnEX7x2_USaYug9xZFv&t=352
"""


# cannot compute the 0th Fibonacci number
def fib1(n):
    """Compute the nth Fibonacci number, for N >= 1."""
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

# can compute the 0th Fibonacci number
def fib2(n):
    """Compute the nth Fibonacci number, for N >= 0."""
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr


def test_for_equivalence():
    assert fib1(0) == fib2(0)
    assert fib1(1) == fib2(1)
    assert fib1(2) == fib2(2)
    assert fib1(3) == fib2(3)
    assert fib1(4) == fib2(4)
    assert fib1(5) == fib2(5)


################################################################################


if __name__ == "__main__":
    test_for_equivalence()
