#!/usr/bin/python3
# File: 101-square.py
# Author: Chidiadi E. Nwosu

"""Define a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a new square

        Args:
            size (int): length of the sides of the square
            position (tuple): position of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns the position of the square to the call function"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the newly created square

        Args:
            value: input parameter for position
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(j >= 0 for j in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """returns the area of the created square"""

        return int(self.size) ** 2

    def my_print(self):
        """that prints in stdout the square with the character #"""
        a = int(self.size)
        b = int(self.position[0])
        c = int(self.position[1])
        if a == 0:
            print()
        else:
            [print() for i in range(c)]
            for j in range(a):
                print(" " * b + "#" * a)

    def __str__(self):
        """returrns the string representation of square"""

        a = int(self.size)
        b = int(self.position[0])
        c = int(self.position[1])
        square = []

        if a == 0:
            square.append("")
        else:
            for i in range(c):
                square.append("")
            for j in range(a):
                square.append(" " * b + "#" * a)
        return "\n".join(square)
