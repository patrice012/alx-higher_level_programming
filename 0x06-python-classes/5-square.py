#!usr/bin/python3

"""
Module Square

Classes:
    Square - A class square
"""


class Square:
    """
    An class square

    Args:
        __size: the size of the square. should be an
        int that's greater than 0
    """

    def __init__(self, size=0):
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
        return self.__size ** 2

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

    def my_print(self):
        """Help to print area of square

        print in stdout the square with the character #
        :if size is equal to 0, print an empty line
        """
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
