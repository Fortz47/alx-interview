#!/usr/bin/python3
"""creates a Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of integers representing
    the Pascal's triangle of n"""
    if n <= 0:
        return []

    res = [[] for i in range(n)]
    res[0].append(1)
    for i in range(1, n):
        for k in range(i + 1):
            val = 1 if k == 0 or k == i else res[i - 1][k - 1] + res[i - 1][k]
            res[i].append(val)
    return res
