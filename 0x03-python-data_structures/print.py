#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    for i in range(1, len(my_list) + 1):
        new_list.append(my_list[-i])
    for j in new_list:
        print("{:d}".format(j))

def reversed(my_list=[]):
    new_list = my_list[::-1]
    for j in new_list:
        print("{:d}".format(j))
