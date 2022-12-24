#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """ returns the Pascal's Triangle of size n. """
    if n <= 0:
        return []

    pascalTriangle = [[1]]
    while len(pascalTriangle) != n:
        last_row = pascalTriangle[-1]
        next_row = [1]

        for i in range(len(last_row) - 1):
            next_row.append(last_row[i] + last_row[i + 1])
        next_row.append(1)
        pascalTriangle.append(next_row)

    return pascalTriangle
