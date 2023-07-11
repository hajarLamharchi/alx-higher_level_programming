#!/usr/bin/python3
""" This module defines the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using
        json representation
    Args:
        my_obj: the obecjt to write
        filename: the text file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
