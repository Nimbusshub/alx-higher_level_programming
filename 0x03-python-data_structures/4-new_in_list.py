#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list
    b = list(my_list)
    for i in range(len(b)):
        if i == idx:
            b[i] = element
    return b
