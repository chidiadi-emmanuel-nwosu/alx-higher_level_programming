#!/usr/bin/python3

# File: 5-no_c.py
# Author: Chidiadi E. Nwosu


def no_c(my_string):
    """no_c - removes all characters c and C from a string


        my_string: input string

    Returns:
        newly created string without c and C
    """
    new_string = ""
    for i in my_string:
        if i not in "cC":
            new_string += i
    return new_string
