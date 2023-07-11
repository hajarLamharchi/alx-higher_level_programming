#!/usr/bin/python3
""" Defines the function from_json_string """
import json


def from_json_string(my_str):
    """ Returns an object represented by json string
    Arg:
        my_str: json representation
    """
    return json.loads(my_str)
