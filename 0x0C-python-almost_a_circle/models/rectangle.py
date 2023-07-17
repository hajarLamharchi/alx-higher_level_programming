#!/usr/bin/python3
""" This module defines the class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Defines the class rectangle by
    Attributes:
        width(int): width of the rectangle
        height(int): height of the rectangle
        x: private instance attribute
        y: private instance attribute
    """
    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width to value """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Rtrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height to value """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ Retrives the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x to value """
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Rtrieves the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y to value """
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the attributes of the class rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Computes the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle in stdout with # """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the class """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }
