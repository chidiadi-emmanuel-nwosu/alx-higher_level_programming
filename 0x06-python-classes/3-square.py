#!/usr/bin/python3
# File: 3-square.py
# Author: Chidiadi E. Nwosu

"""Define a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """initializes a new square

        Args:
            size (int): length of the sides of the square
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """returns the area of the created square"""

        return int(self.__size) ** 2
