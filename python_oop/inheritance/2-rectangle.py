#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry
"""Defines a Rectangle class"""


class Rectangle(BaseGeometry):
    """Represents a Rectangle."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string
