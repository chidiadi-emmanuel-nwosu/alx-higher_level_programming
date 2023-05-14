#!/usr/bin/python3

# File: 4-new_in_list.py
# Author: Chidiadi E. Nwosu

def new_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position
        without modifying the original list

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
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
