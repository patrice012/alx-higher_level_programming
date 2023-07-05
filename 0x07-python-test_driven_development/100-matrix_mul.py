#!/usr/bin/python3
"""
This module contains the matrix_mul function

Usage: matrix_mul(A, B)
A and B are of type List of List (matrice)
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a(list of list): matrice A
        m_b(list of list): matrice B

    Raises:
        TypeError: if matrix or matrix's element are not a list type
        TypeError: if element in the rows are not integer or float or
        rows don't have the same size
        valueError: if matrix or matrix's element is empty
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_lens_a = []
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if False in [type(x) in (int, float) for x in row]:
            raise TypeError("m_a should contain only integers or floats")
        row_lens_a.append(len(row))

    row_lens_b = []
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if False in [type(x) in (int, float) for x in row]:
            raise TypeError("m_b should contain only integers or floats")
        row_lens_b.append(len(row))

    if len(set(row_lens_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(row_lens_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    new_matrix = []
    for index, row in enumerate(m_b):
        new_row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(0, len(m_b)):
                value += row[k] * m_b[k][j]
            new_row.append(value)
        new_matrix.append(new_row)

    return new_matrix
