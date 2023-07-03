#!/usr/bin/python3
""" This module defines a function that:
    prints a new line after each of these characters. ? :
"""


def text_indentation(text):
    """ This function prints a text with 2 new lines after each of
        these characters . ? :
        Args:
        text (str): text input
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    c = 0
    line = ""
    result = ""
    while c < len(text):
        line += text[c]
        if text[c] in ".?:":
            result += line.strip() + "\n\n"
            line = ""
        if c == len(text) - 1:
            result += line.strip()
        c += 1
    print(result, end="")
