#!/usr/bin/python3
""" This module defines the class square
    that inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines the class square by
    attributes:
        inherits attributes from Rectangle
        width = height = size
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes attributes of the class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the value of size """
        return self.width
    @size.setter
    def size(self, value):
        """ Sets the value of size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Updets the attributes of the square """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
