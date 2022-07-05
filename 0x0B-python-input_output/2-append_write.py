#!/usr/bin/python3

"""Function that appends to a .txt file.
"""


def append_write(filename="", text=""):
    """ A simple function that append to a text file.

    Returns:
        Counts (int): the numbers of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a:
        counts = a.write(text)
        return(counts)
