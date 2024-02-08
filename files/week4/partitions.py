def count_partitions(n, m):
    """Return the number of partitions of n using parts up to m.

    The number of partitions of a positive integer n, using parts up to size m,
    is the number of ways in which n can be expressed as the sum of positive
    integer parts up to m in creasing order.

    n - positive integer greater than 0
    m - positive integer greater than 0

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    >>> count_partitions(4, 2)
    3
    >>> count_partitions(5, 2)
    3
    """

    assert n > 0, "n must be greater than 0"
    assert m > 0, "m must be greater than 0"

    def count_partitions_helper(n0, m0):
        # base case 1: there are 0 ways to partition a negative n0
        if (n0 < 0):
            return 0
        # base case 2: there is one way to partition 0, include no parts
        # base case 3: there is one way to partition any n greater than 0 using
        #              parts of size 1
        if (n0 == 0) or (m0 == 1):
            return 1
        return (count_partitions_helper(n0 - m0, m0)
                + count_partitions_helper(n0, m0 - 1))

    return count_partitions_helper(n, m)
