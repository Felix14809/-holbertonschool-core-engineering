#!/usr/bin/env python3
banned = []
for n in range(1, 100):
    if n not in banned:
        doubles = (n % 10) + (n % 10 * 10)
        used = (n / 10) + (n % 10 * 10)
        banned.append(int(used))
        banned.append(int(doubles))
        if n > 1:
            print(", ", end='')
        print("{0:02d}".format(n), end='')
print()
