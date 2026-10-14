#!/usr/bin/env python3
append_write = __import__('append_write').append_write

nb_characters_added = append_write("file_append.txt", "This cool!\n")
print(nb_characters_added)
