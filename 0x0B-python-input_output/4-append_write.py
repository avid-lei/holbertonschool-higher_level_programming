#!/usr/bin/python3

"""
appends string to end of file
returns number of characters added

"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)
