#!/usr/bin/python3
"""add_attribute module
"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible"""

    if (
        not obj or not attr or not value or
        not isinstance(obj, object) or
        isinstance(obj, str) or
        hasattr(obj, attr)
    ):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
