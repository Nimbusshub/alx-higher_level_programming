#!/usr/bin/python3
"""A script that adds all arguments to a pthton list
and save them"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    content = load_from_json_file("add_item.json")
except FileNotFoundError:
    content = []
content.extend(sys.argv[1:])
save_to_json_file(content, "add_item.json")
