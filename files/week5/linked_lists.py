empty = "empty"


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linke list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        length, s = length + 1, rest(s)
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        i, s = i - 1, rest(s)
    return first(s)


def len_link_recursive(s):
    """Return the length of linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    # if s == empty:
    #     raise IndexError("index out of range")
    # else:
    #     if i == 0:
    #         return first(s)
    #     return getitem_link_recursive(rest(s), i-1)
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i-1)


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    if s == empty:
        return t
    return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s), "s must be a linked list."
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    if s == empty:
        return s
    else:
        if f(first(s)):
            return link(first(s), keep_if_link(f, rest(s)))
        return keep_if_link(f, rest(s))


def join_link(s, separator=" "):
    """Return a string of all elements in s seperated by separator."""
    if s == empty:
        return ""
    else:
        if rest(s) == empty:
            return str(first(s))
        return str(first(s)) + separator + join_link(rest(s), separator)


################################################################################


if __name__ == "__main__":
    four = link(1, link(2, link(3, link(4, empty))))
    print(four)
    print(first(four))
    print(rest(four))
    print("length of 'four' ->", len_link(four))
    print("second element of 'four' ->", getitem_link(four, 1))
    # print("fourth element of 'four' ->", getitem_link(four, 4))
    print("length of 'four' [recursive] ->", len_link_recursive(four))
    print("second element of 'four' [recursive] ->",
          getitem_link_recursive(four, 1))
    # NOTE: the following expression raises an error in 'first'
    # print("fourth element of 'four' [recursive] ->",
    #       getitem_link_recursive(four, 4))
    # NOTE: the following expression raises an error in 'last'
    # print("fifth element of 'four' [recursive] ->",
    #       getitem_link_recursive(four, 5))

    print()

    print(extend_link(four, four))
    print(apply_to_all_link(lambda x: x * x, four))
    print(keep_if_link(lambda x: (x % 2) == 0, four))
    print(join_link(four, ", "))
