from hw04 import tree, label

def exp_tree(values):
    """
    Returns the exponential tree that can be made from VALUES
    with the greatest possible root label
    >>> print_tree(exp_tree([5]))
    5
    >>> print_tree(exp_tree([3, 2]))
    9
      3
      2
    >>> print_tree(exp_tree([2, 3, 2]))
    512
      2
      9
        3
        2
    >>> lst = [3, 1, 2, 3]
    >>> print_tree(exp_tree(lst))
    6561
      3
        3
        1
      8
        2
        3
    """
    if len(values) == 1:
        return tree(values[0])
    else:
        def tree_at_split(i):
            base = exp_tree(values[:i])
            exponent = exp_tree(values[i:])
            return tree(label(base) ** label(exponent), [base, exponent])
        trees = [tree_at_split(i) for i in range(1, len(values))]
        return max(trees, key = lambda t: label(t))
