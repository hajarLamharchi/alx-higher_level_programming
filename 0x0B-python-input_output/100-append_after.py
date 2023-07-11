#!/usr/bin/python3
""" This module defines the function append_after """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text after each line contaning
        a specific string
    Args:
        filename: the text file
        search_string: the specific string to search
        new_string: the line of text to insert
    """
    text = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for lines in f:
            text += lines
            if search_string in lines:
                text += new_string

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
