#!/usr/bin/python3
"""
Module contains Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class define square
    """

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
            ValueError: if value < 0
        """
        self.width = value
        self.height = value

    def __init__(self, size, x=0, y=0, id=None):
        """define and create new square base on Rectangle class"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """Define custom str method"""
        cls_name = self.__class__.__name__
        return f'[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}'
