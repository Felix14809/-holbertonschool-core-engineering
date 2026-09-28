#!/usr/bin/env python3
def pow(a, b):
    result = 1
    if b < 0:
        for _ in range(b * -1):
            result *= a
        return 1 / result
    elif b > 0:
        for _ in range(b):
            result *= a
    return result
