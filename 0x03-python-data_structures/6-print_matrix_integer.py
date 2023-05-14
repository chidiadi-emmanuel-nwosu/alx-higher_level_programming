#!/usr/bin/python3

# File: 6-print_matrix_integer.py
# Author: Chidiadi E. Nwosu


def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer - prints a matrix of integers.

    Args:
        matrix: input 2D array
    """
    for i in matrix:
        count = 0
        for j in i:
            if count != len(i) - 1:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
            count += 1
        print()
