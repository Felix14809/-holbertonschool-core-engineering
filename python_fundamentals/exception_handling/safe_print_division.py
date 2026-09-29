#!/usr/bin/env python3
def safe_print_division(a, b):
    sum = 0
    try:
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        print("Inside result: {0}".format(sum))
    return sum
