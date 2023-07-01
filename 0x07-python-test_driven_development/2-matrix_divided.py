"""
Module contains function

purpose: Divide a matrix
Examples:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """Divide matrix elements

    Args:
        matrix(list of list): matrix of integer or float
        div(int or float): number use to divide matrix's elements

    Raises:
        TypeError: if div is not integer or float
        ZeroDivisionError: if div equal 0
        TypeError: if matrix is not a list or matrix's elements are not list or
                    elements in matrix are not int or float
        TypeError: if matrix's elements don't have the same size

    Returns:
        The new matrix
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    new_matrix = []
    sizes = []
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        if False in [type(x) in (int, float) for x in row]:
            raise TypeError(err_msg)
        sizes.append(len(row))
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    if len(set(sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
