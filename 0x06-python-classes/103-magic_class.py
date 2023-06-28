#!/usr/bin/python3
import math
import dis
""" This class defines a circle """


class MagicClass:
    """ This class defines a circle by
        Attribute
        radius (int or float): the radius of the circle
    """
    def __init__(self, radius):
        """ Initializes a new instance of the Class """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Calculates the area of the circle """
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """ Calculates the circumference of the circle """
        return 2 * math.pi * self.__radius

dis.dis(MagicClass)
