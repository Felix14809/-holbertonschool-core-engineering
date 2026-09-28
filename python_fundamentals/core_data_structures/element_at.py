#!/usr/bin/env python3
def element_at(my_list, idx):
    i = 0
    for item in my_list:
        if i == idx:
            return item
        i += 1
    return None
