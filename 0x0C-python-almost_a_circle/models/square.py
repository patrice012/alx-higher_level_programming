#!/usr/bin/python3
"""
Module contains Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class define square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """define and create new square base on Rectangle class"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """
        Define setter for size attrs

        Args:
            value(int): new attrs value
        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Define custom str method"""
        cls_name = self.__class__.__name__
        return f'[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}'

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        __dict = {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }
        return __dict

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2th argument represents x attribute
                - 3th argument represents size attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            for i in range(0, len(args)):
                match i + 1:
                    case 1:
                        if args[i] is not None:
                            self.id = args[i]
                    case 2:
                        self.x = args[i]
                    case 3:
                        self.size = args[i]
                    case 4:
                        self.y = args[i]
        else:
            for key in kwargs:
                if key == 'id' and kwargs[key] is not None:
                    self.id = kwargs.get(key)
                elif key == 'size':
                    self.size = kwargs.get(key)
                elif key == 'x':
                    self.x = kwargs.get(key)
                elif key == 'y':
                    self.y = kwargs.get(key)
