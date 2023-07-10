#!/usr/bin/python3
""" This module defines a class MyInt that inherits form int """


class MyInt(int):
    """ defines a class MyInt that inverted == and != operators """
    def __eq__(self, other):
        """ compare the current object with another object """
        return not super().__eq__(self)

    def __ne__(self, other):
        """ compare the current object with another object """
        return not super().__ne__(self)
