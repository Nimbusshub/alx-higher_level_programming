#!/usr/bin/python3

"""A subclass of class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.size = size
