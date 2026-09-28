#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    i = 0
    for i in range(len(my_list)):
        if i == idx:
            my_list.insert(i, element)
            del my_list[i]
    return my_list
