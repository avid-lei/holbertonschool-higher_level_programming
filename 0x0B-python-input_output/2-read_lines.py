#!/usr/bin/python3

"""
function that reads n lines of a file
prints to stdout

"""


def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        counter = 1
        for line in f:
            print(line)
            if counter == nb_lines:
                return
            else:
                counter += 1
