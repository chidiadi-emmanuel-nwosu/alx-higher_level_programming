#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """simple_delete - deletes a key in a dictionary.

    Args:
        a_dictionary: dictionary input
        key: a_dictionary key input

    Returns:
        updated a_dictionary
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
