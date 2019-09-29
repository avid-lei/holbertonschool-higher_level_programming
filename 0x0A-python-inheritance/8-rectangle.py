#!/usr/bin/python3

"""
Base Geometry class


"""


class BaseGeometry:
    """
    pubic instance methods
    """
    def area(self):
        """
        raise Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

"""
Rectangle class
inherit from Base Geometry

"""


class Rectangle(BaseGeometry):
    """
    Rectangle inherit from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
