#!/usr/bin/python3

# File: 3-print_reversed_list_integer.py
# Author: Chidiadi E. Nwosu


def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list in reverse order.

    Args:
        my_list: list input
    """
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
