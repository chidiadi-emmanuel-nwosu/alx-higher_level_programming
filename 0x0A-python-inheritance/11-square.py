#!/usr/bin/python3
"""rectangle module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialises the class"""

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """returns the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """returns a string format of the class"""
        return f"Square {self.__size}/{self.__size}"
