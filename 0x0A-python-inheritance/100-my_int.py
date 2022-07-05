#!/usr/bin/python3
"""A class that inherits from class int"""


class MyInt(int):
    """Subclass of class int"""

    def __eq__(self, obj):
        """Reverts == function.
        Changes equals to to not equal to."""

        return int.__ne__(self, obj)

    def __ne__(self, obj):
        """Reverts != function.
        Changes not equal to to equals to."""

        return int.__eq__(self, obj)
