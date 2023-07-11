#!/usr/bin/python3
""" defines the function append_write """


def append_write(filename="", text=""):
    """ append text to a file
    Args:
        filename: the to append text to
        text: the text to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
