#!/usr/bin/env python3
"""Defines BaseGeomentry classes"""


class BaseGeometry:
    """Represents a base for geometric shapes."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a Rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        s = "[{}] {}/{}".format(type(self).__name__, self.width, self.height)
        return s


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
