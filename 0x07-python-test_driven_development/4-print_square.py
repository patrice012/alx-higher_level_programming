#!/usr/bin/python3
"""
Module contains one function: print_square
------
Prototype: def print_square(size)
---------
Usage: print_square(integer_number)
-----
"""


def print_square(size):
    """
    Function used to print square of the given number

    Args:
        size(int):  is the size length of the square
    Raises:
        TypeError: When size is not integer
                or size is float and less than 0
        ValueError: When size is less than 0
    """
    if size is None or not type(size) in (int, float):
        raise TypeError("size must be an integer")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, int(size)):
        for j in range(0, int(size)):
            print("#", end="")
        print()
