#!/usr/bin/python3
"""pascal triangle module
"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    tri = []

    if n <= 0:
        return tri
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if not j or j + 1 == i:
                row.append(1)
            else:
                x = tri[i - 2][j - 1] + tri[i - 2][j]
                row.append(x)
        tri.append(row)

    return tri
