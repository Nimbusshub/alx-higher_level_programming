#!/usr/bin/python3
def best_score(a_dictionary):

    value = 0
    key1 = ""

    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > value:
            value = a_dictionary[key]
            key1 = key
    return key1
