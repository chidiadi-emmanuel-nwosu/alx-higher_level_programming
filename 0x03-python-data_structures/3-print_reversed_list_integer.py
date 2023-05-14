#!/usr/bin/python3

# File: 3-print_reversed_list_integer.py
# Author: Chidiadi E. Nwosu


def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list in reverse order.

    Args:
        my_list: list input
    """
    if not my_list:
        return None
    for i in my_list.reverse():
        print("{:d}".format(i))
