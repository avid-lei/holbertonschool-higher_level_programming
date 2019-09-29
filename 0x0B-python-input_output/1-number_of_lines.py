#!/usr/bin/python3

"""
function returns # of lines
in file

"""


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        lnum = 0
        for line in f:
            lnum += 1
        return lnum
