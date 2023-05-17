#!/usr/bin/python3
def uniq_add(my_list=[]):
    """uniq_add - adds all unique integers in a list

    Args:
        my_list: list input

    Returns:
        the sum of unique value of my_list
    """
    return sum(set(my_list))
