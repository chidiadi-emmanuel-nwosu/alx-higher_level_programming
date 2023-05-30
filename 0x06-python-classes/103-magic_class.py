#!/usr/bin/python3
# File: 103-magic_class.py
import math
"""defines a magic class"""


class MagicClass:
    def __init__(self, radius):
        """initializes a circle"""
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """find the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """find the circumference of the circle"""
        return 2 * math.pi * self.__radius
