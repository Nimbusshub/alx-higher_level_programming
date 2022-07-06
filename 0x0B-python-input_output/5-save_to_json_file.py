#!/usr/bin/python3
"""Function that writes an object to a text file using json"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file using json"""
    with open(filename, "w", encoding='utf-8') as a:
        save_it = json.dumps(my_obj)
        a.write(save_it)
