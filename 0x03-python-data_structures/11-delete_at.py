#!/usr/bin/python3

# File: 11-delete_at.py
# Author: Chidiadi E. Nwosu


def delete_at(my_list=[], idx=0):
    """delete_at - deletes the item at a specific position in a list

    Args:
        my_list: list input

    Returns:
        new list without the deleted element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
