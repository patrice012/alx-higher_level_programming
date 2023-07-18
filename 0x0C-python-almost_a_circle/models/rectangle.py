#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representation.
    Represents a rectangle and inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Use to initialise rectangle objects.

        Args:
            width(int or float): rectangle object width
            height(int or float): rectangle object heigh
            x(int or float): rectangle x value
            y(int or float): rectangle y value
            id(int): object id

        Attributes:
            width: rectangle width
            height: rectangle height
            x: x position
            y: y positio
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, n_x):
        """setter for x"""
        if type(n_x) is not int:
            raise TypeError("x must be an integer")
        elif n_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = n_x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, n_y):
        """setter for y"""
        if type(n_y) is not int:
            raise TypeError("y must be an integer")
        elif n_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = n_y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def __str__(self):
        """Return the string representation of the rectangle instance"""
        cls_name ,_id = self.__class__.__name__, self.id
        width ,height = self.__width, self.__height
        x, y = self.__x, self.__y
        return f"[{cls_name}] ({_id}) {x}/{y} - {width}/{height}"

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            for i in range(0, len(args)):
                match i + 1:
                    case 1:
                        if args[i] is not None:
                            self.id = args[i]
                    case 2:
                        self.width = args[i]
                    case 3:
                        self.height = args[i]
                    case 4:
                        self.x = args[i]
                    case 5:
                        self.y = args[i]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                elif key == 'width':
                    self.width = kwargs.get(key)
                elif key == 'height':
                    self.height = kwargs.get(key)
                elif key == 'x':
                    self.x = kwargs.get(key)
                elif key == 'y':
                    self.y = kwargs.get(key)


    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        __dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return __dict
