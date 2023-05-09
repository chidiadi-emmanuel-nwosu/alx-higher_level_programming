#!/usr/bin/python3
def magic_calculation(a, b, c):
    """magic_calculation - compares input integers

    Args:
        a: first integer
        b: second integer
        c: third integer

    Returns:
        c, if a is less than b
        a + b, if b is less than c
        a * b - c, otherwise
    """

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
