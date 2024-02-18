from linked_lists import *


def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    # base case 1: there is one way to partition 0 -> no parts
    if n == 0:
        return link(empty, empty)
    # base case 2/3: there is no way to partition n using 0 or negative numbers
    elif n < 0 or m == 0:
        return empty
    else:
        with_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), with_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


################################################################################


if __name__ == "__main__":
    pall = partitions(2, 2)
    print(pall)
    print()
    print()
    partitions_as_linked_lists = partitions(6, 4)
    print(partitions_as_linked_lists)
    print()
    print(first(partitions_as_linked_lists))
    print()
    print(rest(partitions_as_linked_lists))
    print()
    print(first(rest(partitions_as_linked_lists)))
    print()
    print(rest(rest(partitions_as_linked_lists)))
    print_partitions(6, 4)
