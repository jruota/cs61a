def fib(n):
    """Return the n-th Fibonacci number.

    n -- positive integer >= 1
    """
    prev, curr, i = 0, 1, 2

    if (n == 1):
        return prev
    elif (n == 2):
        return curr

    while i < n:
        prev, curr = curr, curr+prev
        i += 1

    return curr

def fib_test():
    assert fib(1) == 0, "The 1st Fibonacci number should be 0"
    assert fib(2) == 1, "The 2nd Fibonacci number should be 1"
    assert fib(3) == 1, "The 3rd Fibonacci number should be 1"
    assert fib(50) == 7778742049, "Error at the 50th Fibonacci number"

def fibonacci(n):
    """Print the first n Fibonacci numbers.

    n -- positive integer
    """
    prev = 0
    curr = 1
    while n > 0:
        print(prev, end=" ")
        prev, curr = curr, curr+prev
        n -= 1
    print()

################################################################################

if __name__ == "__main__":
    fibonacci(20)
    fib_test()
