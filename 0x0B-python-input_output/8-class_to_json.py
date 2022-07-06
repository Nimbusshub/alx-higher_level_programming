#!/usr/bin/python3

"""A function that gets a dictionary description with simple
data structure using json"""


def class_to_json(obj):
    """Function that returns the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (class): instance of a class to serialize.

    Returns:
        A dictionary description.
    """
    return obj.__dict__
