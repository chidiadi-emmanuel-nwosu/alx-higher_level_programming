#!/usr/bin/python3

# File: 0-print_list_integer.py
# Author: Chidiadi


def print_list_integer(my_list=[]):
    """prints all integers of a list.

    Args:
        my_list: list input
    """
    for i in my_list:
        print("{:d}".format(i))
