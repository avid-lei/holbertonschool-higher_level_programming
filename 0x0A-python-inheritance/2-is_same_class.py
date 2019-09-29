#!/usr/bin/python3

"""
Returns True if obj is instance of class
otherwise False

"""


def is_same_class(obj, a_class):
    if dir(obj) == dir(a_class):
        return True
    return False
