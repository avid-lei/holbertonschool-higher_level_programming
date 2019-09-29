#!/usr/bin/python3

"""
returns True is obj is instance of class
or class inherited from said class
otherwise False
"""


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
