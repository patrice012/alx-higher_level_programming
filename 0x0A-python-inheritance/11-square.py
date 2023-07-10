#!/usr/bin/python3
"""
Module contains Square Class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class
    """
    def __init__(self, size):
        """
        args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Implementation of area method
        """
        return self.__size * self.__size

    def __str__(self):
        """Custom function"""
        name = self.__class__.__name__
        return "[{}] {}/{}".format(name, self.__size, self.__size)
