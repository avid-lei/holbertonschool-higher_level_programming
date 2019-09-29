#!/usr/bin/python3

"""
class Student
public instance attributes

"""


class Student:
    """
    public instances
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves dictionary rep of instance
        """
        return self.__dict__
