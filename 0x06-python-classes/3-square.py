#!/usr/bin/python3
""" A class Square that defines a square """


class Square:
    """A class with a private instance attribute.
    def __init__: initialize class Square.
        It also checks for TypeError and ValueError.

    Args:
        size (int): size of the class Square

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is lesser than 0.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of the current square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size
