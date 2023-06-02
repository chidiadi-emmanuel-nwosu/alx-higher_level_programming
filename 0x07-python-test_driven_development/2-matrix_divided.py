#!/usr/bin/python3
"""Calculaion module
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix \
                (list of lists) of integers/floats')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix \
                    (list of lists) of integers/floats')
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError('matrix must be a matrix \
                        (list of lists) of integers/floats')

    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) is not first_row_len:
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = []
    for row in matrix:
        new.append([round(i / div, 2) for i in row])

    return new
