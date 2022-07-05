#!/usr/bin/python3

"""Function that reads a .txt file and prints to stdout
"""


def read_file(filename=""):
    """ A simple function that reads a text file.
    """
    with open(filename, encoding="utf-8") as a:
        texts = a.read()
    print(texts, end='')
