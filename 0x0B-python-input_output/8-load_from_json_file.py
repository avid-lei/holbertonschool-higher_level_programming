#!/usr/bin/python3

"""
function
creates an Obj from JSON

"""
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
