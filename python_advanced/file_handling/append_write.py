#!/usr/bin/env python3

"""This function appends text to a file"""


def append_write(filename="", text=""):

    """This function appends text to a file and
    return characters added"""

    with open(filename, "a") as f:
        return f.write(text)
