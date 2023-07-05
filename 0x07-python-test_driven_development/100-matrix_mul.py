#!/usr/bin/python3
""" This module defines matrix multiplication """


def matrix_mul(m_a, m_b):
    """ multiplies two matrices
        Args:
        m_a: first matrix
        m_b: second matrix
        Returns: the new matrix
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elm in row:
            if not isinstance(elm, (float, int)):
                raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        for elm in row:
            if not isinstance(elm, (float, int)):
                raise TypeError('m_b should contain only integers or floats')

    size_a = len(m_a[0])
    for row in m_a:
        if len(row) != size_a:
            raise TypeError('each row of m_a must be of the same size')

    size_b = len(m_b[0])
    for row in m_b:
        if len(row) != size_b:
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_m_a = len(m_a)
    col_m_a = len(m_a[0])
    row_m_b = len(m_b)
    col_m_b = len(m_b[0])

    result = [[0] * col_m_b for _ in range(row_m_a)]

    for i in range(row_m_a):
        for j in range(col_m_b):
            for k in range(col_m_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
