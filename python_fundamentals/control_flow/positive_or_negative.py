#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)

if (number > 0):
    print("%d is positive" % number)
elif (number == 0):
    print("%d is zero" % number)
else:
    print("%d is negative" % number)
