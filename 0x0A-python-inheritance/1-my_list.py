#!/usr/bin/python3
"""Mylist module
"""


class MyList(list):
    """calss that inherits from a list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
