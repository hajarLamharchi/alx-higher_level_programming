#!/usr/bin/python3
""" This module defines the class Student """


class Student:
    """ This class defines a student by
    Attributes:
        first_name: string
        last_name: string
        age: int
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes the attributes of the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Rtrieves a dictionary representation of a student """
        return self.__dict__
