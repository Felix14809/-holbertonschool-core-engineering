#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    print("{0}".format(number % 10))
    return number % 10
