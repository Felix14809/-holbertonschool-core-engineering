#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
if number > 0 and number % 10 > 5:
    print(f"Last digit of {number} is {n % 10} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif number < 0 or number % 10 < 6:
    if number < 0:
        i = (number * -1) % 10 * -1
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")
    else:
        i = number % 10
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")
