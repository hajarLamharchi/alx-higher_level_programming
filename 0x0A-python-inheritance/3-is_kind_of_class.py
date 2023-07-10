#!/usr/bin/python3
""" This module defines the function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is an instance of a_class
        otherwise False
        Args:
        obj: the object to check
        a_class: the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
