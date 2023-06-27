#!/usr/bin/python3
""" This class defines a square """


class Square:
    """This class defines a square by
        Attribute:
            size (int): size of the square
    """
    def __init__(self, size=0):
        """ Initializes a new instance of the square
            Parameters:
                size (int): size of the square
                -> The size must be an integer and >= 0
        """
        self.__size = size

    def area(self):
        """ Calculates the area of the square
            Returns:
                int: the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Retrieves the value of size
            Returns:
                int: value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to value"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
