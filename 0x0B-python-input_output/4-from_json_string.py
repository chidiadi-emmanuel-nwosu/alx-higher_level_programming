#!/usr/bin/python3
"""4-to_json_string module
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
       represented by a JSON string
    """
    return json.loads(my_str)
