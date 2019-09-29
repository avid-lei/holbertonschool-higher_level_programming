#!/usr/bin/python3

"""
function
returns dictionary desc with data struct
for JSON serial of abj
"""


def class_to_json(obj):
    return obj.__dict__
