#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply_by_2 - returns a new dictionary with
                       all values multiplied by 2.

    Args:
        a_dictionary: dictionary input

    Returns:
        updated a_dictionary with values multiplied by 2
    """
    new_dict = dict()
    for key, value in map(lambda x: (x[0], x[1] * 2), a_dictionary.items()):
        new_dict[key] = value
    return new_dict
