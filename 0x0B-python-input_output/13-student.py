#!/usr/bin/python3

"""
class Student
public instance attributes

"""
import json


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
        if attrs:
            return {x: obj[x] for x in obj if x in attrs}
        else:
            return obj

    def reload_from_json(self, json):
        """
        replaces all sttr of Student instance
        """
        for key in json:
            setattr(self, key, json[key])
