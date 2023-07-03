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

    str1 = text
    c = 0
    a = 0
    while str1[c] == " ":
        str1 = str1[c + 1 : len(str1) - 1]
        c += 1
    print(str1)
    print(len(str1))
    length = len(str1)
    while str1[length - 1] == " ":
        str1 = str1[0 : length - 2]
        length -= 1
    while a < len(str1):
        print(str1[a], end="")
        if a + 1 < len(str1) and str1[a] in ".?:" and str1[a + 1] == " ":
            a += 1
            print()
            if a + 2 == len(str1) or str1[a + 2] not in ".?:":
                print()
        a += 1
    else:
        if a > 0 and str1[a - 1] in ".?:":
            print()
            print()
