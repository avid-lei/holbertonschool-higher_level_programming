#!/usr/bin/python3

"""
function that writes
object to a text files
using a JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
