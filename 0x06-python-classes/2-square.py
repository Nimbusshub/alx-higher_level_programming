#!/usr/bin/python3
""" A class Square that defines a square """


from typing import Type


class Square:
    """A class with a private instance attribute.
    def __init__: initialize class Square

    Args:
        size (int): size of the class Square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
