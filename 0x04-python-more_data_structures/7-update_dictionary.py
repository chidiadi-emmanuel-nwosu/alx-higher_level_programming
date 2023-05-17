#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """update_dictionary - replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dictionary input
        key: a_dictionary key input
        value: corresponding key element
    """
    a_dictionary[key] = value
    return a_dictionary
