#!/usr/bin/env python3
n = __import__('random').randint(-10000, 10000)
if n > 0 and n % 10 > 5:
    print(f"Last digit of {n} is {n % 10} and is greater than 5")
elif n % 10 == 0:
    print("Last digit of {0} is 0 and is 0".format(n))
elif n % 10 < 6:
    if n < 0:
        i = (n * -1) % 10 * -1
        print(f"Last digit of {n} is {i} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n} is {n % 10} and is less than 6 and not 0")
