#!/usr/bin/python3
""" This module defines a class that:
    prevent users from creating new instance
"""


class LockedClass:
    """ prevents users from dynamically creating new instance attributes,
        except if the new instance attribute is called first_name
    """
    __slots__ = ("first_name",)
    def __setattr__(self, attr_name, attr_val):
        """Override setattr() to restrict the creation of new attributes
           Args:
           attr_name: name of the attribute
           attr_val: value to assign to the attribute
        """
        if hasattr(self, attr_name) or attr_name == "first_name":
            super().__setattr__(attr_name, attr_val)
        else:
            raise AttributeError("")
