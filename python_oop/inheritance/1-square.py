#!/usr/bin/env python3
"""Defines a square class"""


Rectangle = __import__('2-rectangle').Rectangle



class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
