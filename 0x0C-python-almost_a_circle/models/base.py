#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """base class representation.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init the class and set it"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert `list_dictionaries` to JSON string representation

        Args:
            list_dictionaries(list): is a list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                data = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**cls_dict) for cls_dict in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV representation of list_objs to a file"""
        import csv
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a file of JSON strings"""
        import csv
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        from turtle import Turtle, Screen, exitonclick

        WIDTH, HEIGHT = 360, 360

        screen = Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

        trt = Turtle()
        trt.screen.bgcolor("#777")
        trt.pensize(3)
        trt.shape("turtle")

        trt.hideturtle()
        trt.color("#ffffff")
        for rect in list_rectangles:
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()
            for i in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)

        trt.color("#b5e3d8")
        for sq in list_squares:
            trt.up()
            trt.goto(sq.x, sq.y)
            trt.down()
            for i in range(2):
                trt.forward(sq.width)
                trt.left(90)
                trt.forward(sq.height)
                trt.left(90)

        exitonclick()
