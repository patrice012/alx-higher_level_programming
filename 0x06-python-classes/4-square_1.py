#!usr/bin/python3

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

    def area(self):
        """ Calculate the area ot the given square

        Returns:
            area(int): the area of the size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Help to get private attribute value

        Return:
            size: the size of private attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Help to set private attribute value

        Args:
            size(int): new value of hidden attribute

        Raises:
            TypeError: When `size` is not Integer
            ValueError: When `size` is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
