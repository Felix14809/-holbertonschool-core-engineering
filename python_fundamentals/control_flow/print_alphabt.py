#!/usr/bin/env python3
letter = 97
for i in range(25):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{0}".format(chr(letter)))
    letter = letter + 1
