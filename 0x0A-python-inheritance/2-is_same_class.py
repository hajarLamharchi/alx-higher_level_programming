#!/usr/bin/python3
""" this module defiens the function is_same_class """


def is_same_class(obj, a_class):
    """ returns true if ogj is an instance of a_class
        otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
