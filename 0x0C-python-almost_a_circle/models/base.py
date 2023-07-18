#!/usr/bin/python3
""" This module defines the class Base """
import json
import turtle


class Base:
    """ This class manages id attribute in all classes
        to avoid duplicating the same code
    Attributes:
        __nb_objects: private class attriute
        id: public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the class attributes
        Args:
            id(int): id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                s = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation """
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns alist of instances """
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as jfile:
                dicts = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws rectangles and squares """
        s = turtle.getscreen()
        t = turtle.Turtle()
        t.shape("turtle")
        turtle.bgcolor("blue")
        t.pen(pencolor="black", fillcolor="grey", pensize=5, speed=1)
        for instance in list_rectangles:
            t.pen(pencolor="black", fillcolor="grey", pensize=5, speed=1)
            data = instance.to_dictionary()

            t.home()
            t.setpos(data['x'], data['y'])

            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)

        for instance in list_squares:
            data = instance.to_dictionary()
            t.home()
            t.setpos(data['x'], data['y'])
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
            t.pu()

        turtle.getscreen()._root.mainloop()
