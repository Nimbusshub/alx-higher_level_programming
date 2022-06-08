#!/usr/bin/python3
"""
print_sorted_dictionary: prints a sorted dictionary to the console
"""


def print_sorted_dictionary(a_dictionary):
    for keyword in sorted(a_dictionary):
        print(keyword, ":", a_dictionary[keyword])
