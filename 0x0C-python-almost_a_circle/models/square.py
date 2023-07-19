#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size, x=0, y=0, id=None):
        """init the square instance"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the rectangle instance arguments"""
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
        return f"[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """return the dictionary representation of the instance"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
