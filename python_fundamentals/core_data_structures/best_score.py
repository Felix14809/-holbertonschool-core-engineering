#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = None
    for key, v in a_dictionary.items():
        if biggest is None:
            biggest = v
            bigkey = key
        elif v > biggest:
            biggest = v
            bigkey = key
    return bigkey
