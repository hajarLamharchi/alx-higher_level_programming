#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix
        Args:
        matrix: list of lists of integers or floats
        div: dividend integer or float
        Returns:
        new matrix
    """
    if not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(elm, (int, float))
                    for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [[round(elm / div, 2) for elm in row] for row in matrix]

    return result
