#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    size = 0
    value = 0
    for i in my_list:
        value += i[0] * i[1]
        size += i[1]
    return value / size
