#!/usr/bin/env python3

"""This function reads a file"""


def read_file(filename=""):

    """This function reads a file and prints its content"""

    with open(filename) as f:
        print(f.read(), end='')
