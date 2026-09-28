#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for item in row:
            if i is not 0:
                print(" ")
            print("{:d}".format(item), end='')
            i = 1
        print()
