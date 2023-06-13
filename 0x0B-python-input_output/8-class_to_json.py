#!/usr/bin/python3
"""class to json module
"""


def class_to_json(obj):
    """returns the dictionary description with simple
       data structure (list, dictionary, string, integer
       and boolean) for JSON serialization of an object
    """
    return my_obj.__dict__
