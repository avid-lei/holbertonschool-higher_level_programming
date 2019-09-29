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
Parent: Base Geometry class
Child: Rectangle class

"""


class Rectangle(BaseGeometry):
    """
    Rectangle inherit from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init for rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        implement area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

"""
Parent: Base Geometry class
Child: Square class

"""


class Square(Rectangle):
    """
    Square class inherit from rectangle
    """
    def __init__(self, size):
        """
        init for square
        """
        self.__size = size
        super().__init__(self.__size, self.__size)
