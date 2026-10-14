#!/usr/bin/env python3

"""This function writes text to a file"""


def write_file(filename="", text=""):

    """This function writes text to a file and
    return characters written"""

    with open(filename, "w") as f:
        return f.write(text)
