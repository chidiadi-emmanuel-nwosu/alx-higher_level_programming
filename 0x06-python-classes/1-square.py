#!/usr/bin/python3
# File: 1-square.py
# Author: Chidiadi E. Nwosu

"""Define a square class"""


class Square:
    """A square class"""

    def __init__(self, size):
        """initializes a new square

        Args:
            size (int): length of the sides of the square
        """
        self.__size = size
