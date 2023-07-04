#!/usr/bin/python3
""" This module defines a class that:
    prevent users from creating new instance
"""


class LockedClass:
    """ prevents users from dynamically creating new instance attributes,
        except if the new instance attribute is called first_name
    """
    __slots__ = ("first_name")
