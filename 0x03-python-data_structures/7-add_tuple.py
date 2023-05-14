#!/usr/bin/python3

# File: 7-add_tuple.py
# Author: Chidiadi E. Nwosu

def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple - adds 2 tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        tuple wiht 2 integers
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        elif len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        elif len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
