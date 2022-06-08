#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for key1 in a_dictionary:
        if key1 == key:
            a_dictionary[key1] = value
            flag = 1
            break
    if flag == 0:
        a_dictionary[key] = value
    return a_dictionary
