#!/usr/bin/python3

"""module contain class"""


class Square:
    """Class Square that defines a square

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """ Init a private attribute

        Args:
            size(int): Size of the square
        """
        self.__size = size
