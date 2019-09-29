#!/usr/bin/python3

"""
class inheritance
from list

"""


class MyList(list):
    """
    MyList class inherit from list
    """
    def print_sorted(self):
        """
        prints the list sorted
        """
        print(sorted(self))
