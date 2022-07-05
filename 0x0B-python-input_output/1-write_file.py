#!/usr/bin/python3

"""Function that writes to a .txt file.
"""


def write_file(filename="", text=""):
    """ A simple function that writes to a text file.

    Returns:
        Counts (int): the numbers of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a:
        counts = a.write(text)
        return(counts)
