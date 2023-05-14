#!/usr/bin/python3

# File: 2-replace_in_list.py
# Author: Chidiadi E. Nwosu

def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position

    Args:
        my_list: list input
        idx: index to replace element
        element: new element

    Returns:
        a modified list with replaced element
        the original list if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
