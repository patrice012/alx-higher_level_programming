#!/usr/bin/python3
"""
Module contains python base class
"""
import json


class Base:
    """This is the "base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation

        Args:
            list_dictionaries(list): is a list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): is a list of instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        data = []
        if list_objs and len(list_objs) != 0:
            data = [el.to_dictionary() for el in list_objs]
        with open(filename, mode='w') as f:
            if list_objs  is None:
                f.write("{}".format(data))
            else:
                f.write(Base.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from json string

        Args:
            json_string(str): is a string representing a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from dictionary representation"""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            if cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

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

