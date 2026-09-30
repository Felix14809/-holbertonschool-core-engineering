#!/usr/bin/env python3
"""Defines a Rectangle class"""


class Square:
    """Represents a rectangle."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for _ in range(self.__size + 1):
            for n in range(self.__size):
                print('#', end='')
            print()
