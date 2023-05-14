#!/usr/bin/python3

# File: 1-element_at.py
# Author:  Chidiadi E. Nwosu


def element_at(my_list, idx):
    """retrieves an element from a list

    Args:
        my_list: list input
        idx: index of list to retrieve element

    Returns:
        the element at index idx of list my_list
        None if idx is negative or out of range
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
