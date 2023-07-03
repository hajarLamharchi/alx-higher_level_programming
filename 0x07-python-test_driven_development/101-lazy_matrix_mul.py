#!/usr/bin/python3
""" This module multiplies two matrices using NumPy """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrices using NumPy
        Args:
        m_a: first matrix
        m_b: second matrix
    """
    mul = np.matmul(m_a, m_b)
    return mul
