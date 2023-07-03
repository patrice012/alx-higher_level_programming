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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Computes the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Change string representation

        Using # inn place of obj name
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """Return string representation of obj"""
        module = self.__module__
        class_name = self.__class__.__name__
        obj_id = hex(id(self))
        return f'<{module}.{class_name} object at {obj_id}>'
