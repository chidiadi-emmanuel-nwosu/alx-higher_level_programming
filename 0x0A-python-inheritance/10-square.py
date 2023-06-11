#!/usr/bin/python3
"""rectangle module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialises the class"""

        super().__init__(size, size)
