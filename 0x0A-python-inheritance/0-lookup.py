#!//usr/bin/python3
"""Lookup module
"""


def lookup(obj):
    """returns the list of available attributes
       and methods of an object
    """
    if not obj:
        return []
    return dir(obj)
