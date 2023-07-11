#!/usr/bin/python3
""" This module defines the function class_to_json """


def class_to_json(obj):
    """ Return the dictionary description with simple data structure
        for JSON serialization of an object
    Arg:
        obj: is an instance of a class
        all attributes of the obj class are serializable
    """
    return obj.__dict__
