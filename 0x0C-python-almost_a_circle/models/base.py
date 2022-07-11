#!/usr/bin/python3

"""Definition of class Base with its attribute"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that converts the argument to
        its JSON representation.

        Args:
            list_dictionary (dict): list of dictionaries to convert
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                container = cls.to_json_string(list_dict)
                file.write(container)
