#!/usr/bin/python3
"""Student module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """instantiation of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
           of a Student instance
        """
        if (
            isinstance(attrs, list) and
            all(isinstance(attr, str) for attr in attrs)
        ):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
