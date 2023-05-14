#!/usr/bin/python3

# File: 10-divisible_by_2.py
# Author: Chidiadi E. Nwosu


def divisible_by_2(my_list=[]):
    """divisible_by_2 - finds all multiples of 2 in a list.

    Args:
        my_list: list input

    Returns:
        a new list with True or False, depending on whether the integer
        at the same position in the original list is a multiple of 2
    """
    div_list = []
    for i in my_list:
        if i % 2 == 0:
            div_list.append(True)
        else:
            div_list.append(False)
    return div_list
