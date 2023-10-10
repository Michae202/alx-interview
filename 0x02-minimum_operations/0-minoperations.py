#!/usr/bin/python3
""" Minimum Operation module for calculating minimum operation """


def minOperations(n: int) -> int:
    """
    Returns a dictionary representing the prime factorization of a number.
    The keys of the dictionary are the prime factors, and the values are
    the corresponding exponents.
    """
    if not isinstance(n, int):
        return 0

    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    copy = 0
    paste = 0
    clipboard = ''
    hlist = 'H'

    while len(hlist) < n:
        if len(hlist) in factors:
            copy += 1
            clipboard = hlist

        paste = paste + 1
        hlist = hlist + clipboard

    operations = copy + paste
    return operations
