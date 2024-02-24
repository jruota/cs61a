from tree import *


def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t for which
    the labels along the path sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    # if (total - label(t) == 0):
    #     return 1 + sum([count_paths(b, total - label(t)) for b in branches(t)])
    # return sum([count_paths(b, total - label(t)) for b in branches(t)])
    below_current_node = sum(
        [count_paths(b, total - label(t)) for b in branches(t)])
    if (total == label(t)):
        return 1 + below_current_node
    return below_current_node
