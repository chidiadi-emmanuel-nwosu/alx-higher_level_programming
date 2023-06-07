#!/usr/bin/python3
"""Print square module
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size: the size length of the square
    """

    if (isinstance(size, float) and size < 0) or (not isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size != 0:
        for i in range(size):
            print("#" * size)
