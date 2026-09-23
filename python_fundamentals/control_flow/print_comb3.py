#!/usr/bin/env python3
for i in range(10):
    for n in range(i + 1, 10):
        if i > 0 or n > 1:
            print(", ", end='')
        print("{0}{1}".format(i, n), end='')
print()