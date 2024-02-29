from hw04 import tree, label, branches, is_leaf


def max_path(t, k):
    """Return a list of the labels on any path in tree t of length at most k
    with the greatest sum.

    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    def helper(t, k, on_path):
        if k <= 0:
            return []
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(b, k-1, True) for b in branches(t)]
        if on_path:
            return max(a, key = lambda x: sum(x))
        else:
            b = [helper(b, k, False) for b in branches(t)]
            return max(a + b, key = lambda x: sum(x))
    return helper(t, k, False)
