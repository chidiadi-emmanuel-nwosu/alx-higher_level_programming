#!/usr/bin/python3
# File: 4-square.py
# Author: Chidiadi E. Nwosu

"""Define a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """initializes a new square

        Args:
            size (int): length of the sides of the square
        """

        self.size = size

    @property
    def size(self):
        """returns the value of size to the call function"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value of the newly created square

        Args:
            size: input parameter for size
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area of the created square"""

        return int(self.size) ** 2
