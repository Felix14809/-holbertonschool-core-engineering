#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    sum = a
    for n in range(b - 1):
        sum = sum * a
    return sum
