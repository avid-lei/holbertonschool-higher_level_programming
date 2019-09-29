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

    def to_json(self, attrs=None):
        """
        retrieves dictionary rep of instance
        """
        obj = self.__dict__
        if attrs is None or attrs == []:
            return obj
        else:
            return {x: obj[x] for x in obj if x in attrs}
