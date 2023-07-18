#!/usr/bin/python3
"""
Module contains Rectangle class
"""
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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Return Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set Rectangle width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value  

    @property
    def height(self):
        """Return Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set Rectangle height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Return Rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set Rectangle x value"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Return Rectangle x"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set Rectangle y value"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __str__(self):
        """Return the string representation of the rectangle instance"""
        cls_name ,_id = self.__class__.__name__, self.id
        width ,height = self.__width, self.__height
        x, y = self.__x, self.__y
        return f"[{cls_name}] ({_id}) {x}/{y} - {width}/{height}"
        
    def area(self):
        """
        Returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
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
                # if key == "id" and kwargs[key] is None:
                #     # self.__init__(self.width, self.height, self.x, self.y)
                #     pass
                # else:
                if key == 'id' and kwargs[key] is not None:
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
