#!/usr/bin/env python3
letter = 97
for i in range(26):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{0}".format(chr(letter)), end='')
    letter = letter + 1
