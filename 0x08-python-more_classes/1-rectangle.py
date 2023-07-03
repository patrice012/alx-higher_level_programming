#!/usr/bin/python3
"""
Module contains an empty class Rectangle

Contains: Rectangle

Use case: Rectangle(1, 5) or Rectangle()
"""


class Rectangle:
    """
    Class contains Getter and Setter

    This class change the behavior of private attrs
    """
    def __init__(self, width=0, height=0):
        """Create new class instance with default attributes

        Args:
            width(int): the Width of the rectangle instance
            height(int): the height of the rectangle instance
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter  to retrieve the object width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set new object width value

        Args:
            value(int): the new width value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter  to retrieve the object height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set new object height value

        Args:
            value(int): the new height value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if isinstance(value, int) and value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
