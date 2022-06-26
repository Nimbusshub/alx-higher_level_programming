#!/usr/bin/python3
""" A class Square that defines a square """


class Square:
    """A class with private instance attributes.
    def __init__: initialize class Square.

    Args:
        size (int): size of the class Square.
        position (tuple): position of the class Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """property getter: retrive the value of size.

        Returns:
            int: the set instance attribute.

        size.setter: set the value of self.__size.
        It also checks for TypeError and ValueError.

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

    @property
    def position(self):
        """property getter: retrive the value of position.

        Returns:
            int: the set instance attribute.

        position.setter: set the value of self.__position.
        It also checks for TypeError.

        Args:
            value (tuple): value to initialize self.__position with.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
            value[0] is not int or value[1] is not int or
                value[0] < 0 or value[1] < 0 or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        # if (not isinstance(value, tuple) or
        #     len(value) != 2 or
        #         not all(isinstance(num, int) for num in value) or
        #         not all(num >= 0 for num in value)):
        #     raise TypeError("position must be a tuple of 2 positive integers")
        # self.__position = value

    def area(self):
        """calculates the area of the current square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #. """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            print("#" * self.__size)
