#!/usr/bin/python3
""" This module defines the function inherits_from """


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a class
        that inherits from a_class otherwise False
        Args:
        obj: the object to check
        a_class: the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
