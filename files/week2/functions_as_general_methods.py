"""Implementation of a general method for iterative refinement.

Used to compute the golden ration, often called phi.

Among the well-known properties of the golden ratio are that it can be computed
by repeatedly summing the inverse of any positive number with 1, and that it is
one less than its square. We can express these properties as functions to be
used with improve.
"""


from math import sqrt


def improve(update, close, guess=1):
    """General method for iterative refinement.

    An iterative improvement algorithm begins with a guess of a solution to an
    equation. It repeatedly applies an update function to improve that guess,
    and applies a close comparison to check whether the current guess is "close
    enough" to be considered correct.

    This improve function is a general expression of repetitive refinement. It
    doesn't specify what problem is being solved: those details are left to the
    update and close functions passed in as arguments.

    update -- function to return a new guess, returns a number
    close -- function to test the current guess, returns a boolean
    guess -- first guess for a solution, number
    """
    while not close(guess):
        guess = update(guess)
    return guess


def improve_test():
    phi = 1/2 + sqrt(5)/2  # closed-form solution to phi
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), "phi differs from its approximation"


def golden_update(guess):
    return 1/guess + 1


def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


################################################################################

if __name__ == "__main__":
    print(improve(golden_update, square_close_to_successor))
    improve_test()
