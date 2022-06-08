#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for key1 in a_dictionary:
        if key1 == key:
            del a_dictionary[key1]
            break
    return a_dictionary
