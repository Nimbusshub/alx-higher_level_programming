#!/usr/bin/python3

"""Definition of class Base with its attribute"""


class Base:
    """Define the class Base with class constructor

    Args:
        id (int): the identity of the instance of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
