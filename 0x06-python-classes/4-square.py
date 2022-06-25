#!/usr/bin/python3
""" A class Square that defines a square """


class Square:
    """A class with a private instance attribute.
    def __init__: initialize class Square.
        It also checks for TypeError and ValueError.

    Args:
        size (int): size of the class Square.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property getter: retrive the value of size.

        Returns:
            int: the set instance attribute.

        size.setter: set the value of self.__size.

        Args:
            value (int): value to initialize self.__size with.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is lesser than 0.

        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the area of the current square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size
