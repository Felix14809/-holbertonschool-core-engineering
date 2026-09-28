#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = False
        for item in row:
            print(" "if space else "", end='')
            print("{:d}".format(item), end='')
            space = True
        print()
