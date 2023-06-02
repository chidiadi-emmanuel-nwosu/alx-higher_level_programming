#!/usr/bin/python3
"""

    Calculaion module

"""


def add_integer(a, b=98):
    """
        adds two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b
