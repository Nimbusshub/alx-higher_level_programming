#!/usr/bin/python3
"""Function that serialized a data with json.
"""
import json


def to_json_string(my_obj):
    """ A simple function that serialized a data with json.

    Returns:
        Serialized (str): the JSON representation of an object.
    """
    serialized = json.dumps(my_obj)
    return(serialized)
