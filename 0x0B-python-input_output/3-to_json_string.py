#!/usr/bin/python3
""" Defines the function to_json_string """
import json


def to_json_string(my_obj):
    """ Returns the json representation of an object
    Arg:
        my_obj: the object to represent
    """
    return json.dumps(my_obj)
