#!/usr/bin/python3
# File: 103-magic_class.py
# Author: Chidiadi E. Nwosu

"""Defines MagicClass that reproduces a code from a Python bytecode"""


import math


class MagicClass:
    """Creates a circle """

    def __init__(self, radius=0):
        """initializes a circle

        Args:
            radius: input radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """find the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """find the circumference of the circle"""
        return 2 * math.pi * self.__radius
