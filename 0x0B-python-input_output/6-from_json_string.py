#!/usr/bin/python3

"""
Function that
returns object rep
by JSON string
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
