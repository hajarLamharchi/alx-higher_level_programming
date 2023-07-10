#!/usr/bin/python3
""" this module defines a class MyList that inherits from list """


class MyList(list):
    """ class that inherits from list """
    def print_sorted(self):
        """ prints the list sorted """
        alist = sorted(self)
        print(alist)
