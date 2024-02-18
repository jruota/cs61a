from tree import tree, label, branches, is_tree, is_leaf


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m.

    The left (index 0) branch contains all ways of partitioning n using at least
    one m.
    The right (index 1) branch contains partitions using parts up to m-1.
    The root label is m.
    """

    # base case 1: there is one way to partition 0 -> no parts
    if n == 0:
        return tree(True)
    # base case 2/3: there is no way to partition n using 0 or negative numbers
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


################################################################################


if __name__ == "__main__":
    print(partition_tree(2, 2))

    print()
    print()

    pt64 = partition_tree(6, 4)
    print(pt64)
    print_parts(pt64)
    print()
    print(branches(pt64)[0])
    print_parts(branches(pt64)[0])
