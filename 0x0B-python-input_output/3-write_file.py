#!/usr/bin/python3

"""
write string to text file
returns number of characters written

"""


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)
