#!/usr/bin/python3
"""
Module contains Function is_same_class

Prototype: def is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class

    return True  if it's the same, otherwise False
    """
    return type(obj) == a_class
