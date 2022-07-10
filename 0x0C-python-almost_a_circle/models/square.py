#!/usr/bin/python3
"""A class Square that inherits from class Rectangle"""

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

    @property
    def size(self):
        """property getter: retrieve the value of size
        of the Square

        size.setter: set the value of self.__width.
        Args:
            value(int): value to initialize self.width with.

        Exceptions: Raises
        TypeError: if value is not an integer
        ValueError: if value is <= 0
        """
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
