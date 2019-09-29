#!/usr/bin/python3

"""
add attribute if possible
or raise TypeError

"""


def add_attribute(obj, attr, val):
    """
    check if obj is instance of non built in class
    """
    if not obj.__class__.__module__ == 'builtins':
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
