#!/usr/bin/python3
"""Checks if an object is the instance of a class"""


def is_same_class(obj, a_class):
    """Function to check if an object is same as a class
    Args:
            obj: the object to verify
            a_class: the class

    Returns:
            True: if it's an instance of the class
            False: if it's not an instance of the class.
    """
    if type(obj) is a_class:
        return True
    return False
