#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible"""

    if (
        not isinstance(obj, object) or
        isinstance(obj, str) or
        hasattr(obj, attr)
    ):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
