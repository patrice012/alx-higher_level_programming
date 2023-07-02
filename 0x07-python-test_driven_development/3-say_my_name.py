"""
Module contains one function say_my_name()

function prototype: def say_my_name(first_name, last_name="")

Usage: ``say_my_name(first_name, last_name)`` or
        ``say_my_name(first_name)``
"""


def say_my_name(first_name, last_name=""):
    """
    Function use to print user name

    Args:
        first_name(str): first argument
        last_name(str): second and last argument

    Raises:
        TypeError: When first_name or last_name is not strings

    Usage:
        say_my_name(first_name, last_name)
    """
    if ((not first_name) or (type(first_name) is not str)
            or first_name == ""):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    try:
        float(first_name)
    except ValueError:
        pass
    else:
        raise TypeError("first_name must be a string")
    try:
        float(last_name)
    except ValueError:
        pass
    else:
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
