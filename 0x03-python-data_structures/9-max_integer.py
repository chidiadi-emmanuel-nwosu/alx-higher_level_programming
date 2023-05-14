#!/usr/bin/python3

# File: 9-max_integer.py
# Author: Chidiadi E. Nwosu


def max_integer(my_list=[]):
    """max_integer - finds the biggest integer of a list

    Args:
        my_list: list input

    Returns:
        the max value in my_list or None if list is empty
    """
    if len(my_list) == 0:
        return None

    _max = 0
    for i in my_list:
        if i > _max:
            _max = i
    return _max
