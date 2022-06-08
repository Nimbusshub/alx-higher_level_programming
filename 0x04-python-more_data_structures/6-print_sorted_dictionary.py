#!/usr/bin/python3
"""
print_sorted_dictionary: prints a sorted dictionary to the console
"""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
