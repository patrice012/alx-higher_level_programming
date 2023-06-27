#!/usr/bin/python3

"""module contain class"""


class Square:
    """Class Square that defines a square

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """

    def __init__(self, size=0):
        """ Init a private attribute

        Args:
            size(int): Size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
