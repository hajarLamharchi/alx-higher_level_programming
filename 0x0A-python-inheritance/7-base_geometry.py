#!/usr/bin/python3
""" This module defines the class BaseGeometry """


class BaseGeometry:
    """ This class defines:
        public instance method: area()
        public instance method: integer_validator()
    """
    def area(self):
        """ raises an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates the value
            args:
            name: always a string
            value: integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
