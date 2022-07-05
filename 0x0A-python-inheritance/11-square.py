#!/usr/bin/python3

"""A subclass of class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Defines the behaviour of the function when printed"""

        print("[Square] {:d}/{:d}".format(self.__size, self.__size), end="")

        return ""
