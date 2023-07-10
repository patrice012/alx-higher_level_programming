#!/usr/bin/python3
"""
Module contains empty class BaseGeometry
"""


class BaseGeometry:
    """
    An empty class BaseGeometry
    """
    def area(self):
        """
        Empty area method

        Raises:
            Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            value(int): BaseGeometry value
            name(str): BaseGeometry name

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less oor equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
