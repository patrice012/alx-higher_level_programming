"""
Module that contains one function

add_interger: performs simple addition between two integer or floats numbers
Examles:
    add_integer(10, 5)
"""


def add_integer(a, b=98):
    """Simple function that adds 2 integers.

    Args:
        a(int or float): first value
        b(int or float): second value
    Raises:
        TypeError: if a or b are not integers or floats
    Returns:
        a + b value
    """
    add = 0
    if not a or (type(a) not in (int, float)):
        raise TypeError("a must be an integer")
    if not b or (type(b) not in (int, float)):
        raise TypeError("b must be an integer")
    add = int(a) + int(b)
    return add
