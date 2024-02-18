from tree import is_leaf, tree


def right_binarize(tree):
    """Construct a right-branching binary tree."""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


################################################################################


if __name__ == "__main__":
    odd_tree = tree(1, [
        tree(2, [tree(5)]),
        tree(3, [tree(6), tree(7)]),
        tree(4, [
            tree(8, [tree(11), tree(12), tree(13), tree(14)]),
            tree(9),
            tree(10)])
    ])
    print(odd_tree)
    print()
    binarized_tree = right_binarize(odd_tree)
    # print(binarized_tree) -> does not work

    # NOTE:
    # The text says
    #   A common tree transformation called binarization computes a binary tree
    #   from an original tree by grouping together adjacent branches.
    # but right-binarize seems to work on one dimensional lists only.
