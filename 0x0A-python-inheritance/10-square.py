#!/usr/bin/python3
""" This module defines the class Square
    that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ this class defines a square by
        Attribute:
        size (int): size of the square
    """
    def __init__(self, size):
        """ Initialize the size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
