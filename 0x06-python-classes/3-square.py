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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area of the square
            Returns:
            int: the area of the square
        """
        return size * size
