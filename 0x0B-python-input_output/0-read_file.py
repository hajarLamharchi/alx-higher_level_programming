#!/usr/bin/python3
""" defines the functions read_file """


def read_file(filename=""):
    """ Reads a text file and prints it to stdout
    Args:
        filename: the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
