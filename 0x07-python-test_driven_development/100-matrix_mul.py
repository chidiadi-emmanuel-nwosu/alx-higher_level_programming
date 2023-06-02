#!/usr/bin/python3
"""Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    # check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    # check if m_a and m_b are list of lists
    if len(m_a) and not any(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if len(m_b) and not any(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    # check if list is empty
    if not len(m_a) or not any(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b) or not any(row for row in m_b):
        raise ValueError("m_b can't be empty")

    # check if list contains only integrs and floats
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError('m_b should contain only integers or floats')

    # check if all rows in the lists are of same size
    m_a_row = len(m_a[0])
    if any(len(row) != m_a_row for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    m_b_row = len(m_b[0])
    if any(len(row) != m_b_row for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # check if m_a and m_b can be multiplied
    if m_a_row != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # performing matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)
    return result
