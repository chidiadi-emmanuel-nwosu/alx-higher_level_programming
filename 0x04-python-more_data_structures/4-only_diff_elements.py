#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """only_diff_elements - returns a set of all elements
                            present in only one set.

    Args:
        set_1: first set input
        set_2: second set input

    Returns:
        new list containing common elements
    """
    return set_1.symmetric_difference(set_2)
