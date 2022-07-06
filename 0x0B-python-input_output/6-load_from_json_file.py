#!/usr/bin/python3
"""A function that creates an object from a "json fle" """
import json


def load_from_json_file(filename):
    """A function that create an object from json file

    Args:
        filename: the .json file to read from
    """
    with open(filename, "r", encoding='utf-8') as content:
        cont = content.read()
        save_it = json.loads(cont)
        return save_it
