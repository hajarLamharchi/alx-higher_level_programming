#!/usr/bin/python3
""" This module defines the function load_from_json_file """
import json


def load_from_json_file(filename):
    """ Creates an object from a json file
    Args:
        filename: text file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
