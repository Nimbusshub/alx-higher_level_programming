#!/usr/bin/python3
"""Checks if an object is the instance of a class or inherits from
a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Function to check if an object is same as a class or
    a subclass
    Args:
            obj: the object to verify
            a_class: the class

    Returns:
            True: if it's an instance of the  class or subclass
            False: if it's not an instance of the class or subclass.
    """
    if isinstance(obj, a_class):
        return True
    return False
