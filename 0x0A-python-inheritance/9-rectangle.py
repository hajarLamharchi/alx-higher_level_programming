#!/usr/bin/python3
""" This module defines the class Rectangle
    that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ this class defines a rectengle by
        Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width, height):
        """ initializes width and height of the rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ computes the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
