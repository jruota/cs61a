def luhn_sum(n):
    """
    >>> luhn_sum(138743)
    30
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def split(n):
    return n // 10, n % 10


################################################################################


def luhn_iterative(n):
    """
    >>> luhn_iterative(138743)
    30
    """
    i, luhn_sum = 1, 0
    while n > 0:
        n, last = split(n)
        if i % 2 == 0:
            luhn_sum += sum_digits(2 * last)
        else:
            luhn_sum += sum_digits(last)
        i += 1
    return luhn_sum
