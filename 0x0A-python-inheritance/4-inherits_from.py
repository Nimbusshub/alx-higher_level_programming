#!/usr/bin/python3
"""Checks if an object is the instance of a subclass
"""


def inherits_from(obj, a_class):
    """Function to check if an object inherits from a subclass
    Args:
            obj: the object to verify
            a_class: the class

    Returns:
            True: if it's an instance of the subclass
            False: if it's not an instance of the subclass
    """
    if type(obj) is a_class:
        return False
    a = isinstance(obj, a_class)
    return a
