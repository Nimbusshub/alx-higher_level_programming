#!/usr/bin/python3
"""A function that list the available attributes and
methods of an object"""


from click import pass_context


def lookup(obj):
    "returns the available attributes of an object"

    return dir(obj)
