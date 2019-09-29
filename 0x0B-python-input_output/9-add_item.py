#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

"""
script adds all arguments to python list
saves to file

"""


filename = "add_item.json"

try:
    obj = load_from_json_file(filename)
except:
    obj = []
finally:
    for x in sys.argv[1:]:
        obj.append(x)
    save_to_json_file(obj, filename)
