#!/usr/bin/python3
"""
this is the add function module
"""
def add_integer(a, b=98):
    """ this function adds two integers
        Args:
        a (int or float): first input
        b (int or float): second input
        Return:
        integer addition of a and b
    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int (a)
    elif isinstance(b, float):
        b = int (b)
    return int(a + b)
