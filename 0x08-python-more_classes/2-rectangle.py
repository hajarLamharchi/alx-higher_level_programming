#!/usr/bin/python3
""" This module defines a class Rectangle """


class Rectangle:
    """ This class defines a rectangle by:
        Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    @property
    def height(self):
        """ Retrieves the value of height
            Returns:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height to value """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """ Retrieves the value of width
            Returns:
            value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width to value """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of the rectangle
            Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
