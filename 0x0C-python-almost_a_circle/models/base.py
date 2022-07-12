#!/usr/bin/python3
"Definition of class Base with its attribute"""

import json
import os
import csv


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
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list of instances): List of instances
            that inherits from class Base.
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w", encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                container = cls.to_json_string(list_dict)
                file.write(container)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, encoding="utf-8") as file:
                json_dict = cls.from_json_string(file.read())
                return [cls.create(**jd) for jd in json_dict]
        except IOError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins

    # @staticmethod
    # def draw(list_rectangles, list_squares):
    #     """Draw Rectangles and Squares using the turtle module.
    #     Args:
    #         list_rectangles (list): A list of Rectangle objects to draw.
    #         list_squares (list): A list of Square objects to draw.
    #     """
    #     turt = turtle.Turtle()
    #     turt.screen.bgcolor("#b7312c")
    #     turt.pensize(3)
    #     turt.shape("turtle")

    #     turt.color("#ffffff")
    #     for rect in list_rectangles:
    #         turt.showturtle()
    #         turt.up()
    #         turt.goto(rect.x, rect.y)
    #         turt.down()
    #         for i in range(2):
    #             turt.forward(rect.width)
    #             turt.left(90)
    #             turt.forward(rect.height)
    #             turt.left(90)
    #         turt.hideturtle()

    #     turt.color("#b5e3d8")
    #     for sq in list_squares:
    #         turt.showturtle()
    #         turt.up()
    #         turt.forward(sq.x, sq.y)
    #         turt.down()
    #         for i in range(2):
    #             turt.forward(sq.width)
    #             turt.left(90)
    #             turt.forward(sq.height)
    #             turt.left(90)
    #         turt.hideturtle()

    #     turtle.exitonclick()
