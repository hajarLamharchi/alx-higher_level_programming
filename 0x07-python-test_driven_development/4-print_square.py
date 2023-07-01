#!/usr/bin/python3
""" This module defines a function that prints a square """


def print_square(size):
    """ This function prints a square with the character #
        Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if not size >= 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for i in range(size):
            print('#', end="")
        print()
