import sys
sys.path.insert(0, "../../tools")
from tracer import tracer


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

#@tracer
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        #print("\t\tDEBUG: left ->", left, type(left), label(left))
        #print("\t\tDEBUG: right ->", right, type(right), label(right))
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

# NOTE: returning tree(n, [left, right]) would be wrong, because n is the index
#       of a Fibonacci number, not a Fibonacci number itself. This recursive
#       function makes sure that the first trees to get their label are leafs
#       whose labels are 0 or 1, and only then do trees higher up get their
#       labels from those. This ensures that all labels are actual Fibonacci
#       numbers.


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
        # NOTE: this version assumes that a tree always has 2 and only 2
        #       branches
        #tree_branches = branches(tree)
        #return count_leaves(tree_branches[0]) + count_leaves(tree_branches[1])


################################################################################

if __name__ == "__main__":
    t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    print(t)
    print(label(t))
    print(branches(t))
    print(label(branches(t)[1]))
    print(is_leaf(t))
    print(is_leaf(branches(t)[0]))
    print(is_leaf(branches(t)[1]))
    print(branches(t)[1])
    #print(is_leaf(branches(t)[1][0]))  # fails, because selects label
    #print(is_leaf(branches(t)[0][1]))  # fails, index out of range
    print(branches(t)[1][0])
    print(is_leaf(branches(branches(t)[1])[0]))
    print(is_leaf(branches(branches(t)[1])[1]))

    print()

    fibo5 = fib_tree(5)
    print(fibo5)
    print(count_leaves(fibo5))
