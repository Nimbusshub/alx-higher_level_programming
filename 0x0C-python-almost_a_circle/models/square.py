#!/usr/bin/python3
"""A class Square that inherits from class Rectangle"""

from ctypes import sizeof
from re import X
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from class Rectangle.

    It's initialized with:
    Args:
        size (int): size of the width and height of Square
        x=0 (int):
        y=0 (int):
        """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Define the behaviour of the class Square"""
        class_name = "[Square] "
        class_id = "({}) {}/{}".format(self.id, self.x, self.y)
        class_size = " - {}".format(self.width)

        return class_name + class_id + class_size
