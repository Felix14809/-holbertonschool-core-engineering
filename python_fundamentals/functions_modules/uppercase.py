#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 123:
            chr(ord(char) - 32)
    print("{0}".format(str))
 