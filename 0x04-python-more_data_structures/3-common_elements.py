#!/usr/bin/python3
def common_elements(set_1, set_2):
    """common_elements - returns a set of common elements in two sets.

    Args:
        set_1: first set input
        set_2: second set input

    Returns:
        new list containing common elements
    """
    return set_1.intersection(set_2)
