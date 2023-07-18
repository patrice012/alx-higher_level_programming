#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class define Square representation
    """
    def __init__(self, size, x=0, y=0, id=None):
        """define and create new square base on Rectangle class"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter for size"""
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
                j = i + 1
                if j == 1:
                    self.id = args[i]
                elif j == 2:
                    self.size = args[i]
                elif j == 3:
                    self.x = args[i]
                elif j == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                elif key == "size":
                    self.size = kwargs.get(key)
                elif key == "x":
                    self.x = kwargs.get(key)
                elif key == "y":
                    self.y = kwargs.get(key)

    def __str__(self):
        """return the string representation of the square instance"""
        cls_name = self.__class__.__name__
        return f'[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}'

    def to_dictionary(self):
        """return the dictionary representation of the instance"""
        __dict = {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }
        return __dict
