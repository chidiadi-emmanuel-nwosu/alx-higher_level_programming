#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """creates a new rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiates a new rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        w = int(self.width)
        h = int(self.height)

        return w * h

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        w = int(self.width)
        h = int(self.height)

        if not w or not h:
            return 0
        return w * 2 + h * 2

    def __str__(self):
        """returns the string representation of the rectangle"""
        w = int(self.width)
        h = int(self.height)
        res = []

        if not w or not h:
            return ""
        res = [str(self.print_symbol) * w for i in range(h)]
        return "\n".join(res)

    def __repr__(self):
        """return a string representation of the rectangle to
           be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """detects when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
