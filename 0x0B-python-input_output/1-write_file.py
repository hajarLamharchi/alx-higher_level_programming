#!/usr/bin/python3
""" defines the function write_file """


def write_file(filename="", text=""):
    """ writes to a file and returns number of characters
    Args:
        filename: the file to write to
        text: the text to write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
