#!/usr/bin/python3
""" defines a function that adds a new attribute to an object """


def add_attribute(obj, name, value):
    """ adds an attribute to an object if it's possible
        Args:
        obj: the object
        name: name of the attribute
        value: value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
