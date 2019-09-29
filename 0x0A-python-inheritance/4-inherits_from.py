#!/usr/bin/python3

"""
returns True if object is instance of class
that inherited from said class
otherwise False
"""


def inherits_from(obj, a_class):
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
