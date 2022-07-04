#!/usr/bin/python3
"""a subclass"""


class MyList(list):
    """a class that inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
