#!/usr/bin/python3
"""Function that deserialized a data with json.
"""
import json


def from_json_string(my_str):
    """ A simple function that deserialized a string with json.

    Returns:
        deserialized (str: the JSON representation as a string.
    """
    deserialized = json.loads(my_str)
    return(deserialized)
