#!/usr/bin/python3
""" This class defines a square """


class Square:
    """ This class defines a square by
        Attribute:
        size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new instance of the square
            Parameters:
            size (int): size of the square
            position (int, int): tuple of two positive integers
        """
        self.size = size
        self.position = position

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
        """ Sets size to value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints the square with the characters # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """ Retrieves the position value
        Returns:
        (int, int): tuple of integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position """
        if not isinstance(value, tuple) \
                or len(value) != 2 \
                or not all(isinstance(n, int) for n in value) \
                or any(n < 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ Prints the square with the characters # """
        string = ""
        if self.__size == 0:
            return string
        else:
            for i in range(self.__position[1]):
                string = string + '\n'
            for i in range(self.__size):
                val = " " * self.__position[0] + "#" * self.__size + '\n'
                string = string + val
        return string
