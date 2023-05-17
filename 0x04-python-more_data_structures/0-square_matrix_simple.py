#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square_matrix_simple - computes the
       square value of all integers of a matrix
    """
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
