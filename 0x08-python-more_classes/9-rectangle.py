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

    Attributes:
        number_of_instances(int): current count of class's objects
        print_symbol(Any Type): Used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create new class instance with default attributes

        Args:
            width(int): the Width of the rectangle instance
            height(int): the height of the rectangle instance
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1

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
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Return string representation of obj"""
        class_name = self.__class__.__name__
        return f'{class_name}({self.__width}, {self.__height})'

    def __del__(self):
        """Return information after object was deleted"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area

        used to find and return  the biggest rectangle based on the area

        Args:
            rect_1(instance of Rectangle): first object
            rect_2(instance of Rectangle): second object

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle class

        Returns:
             Rectangle object
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size

        Args:
            size(int): new instance size

        Returns:
            Square object base on Rectangle class
        """
        return (cls(size, size))
