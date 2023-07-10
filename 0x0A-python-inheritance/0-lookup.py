#!/usr/bin/python3
"""
Define Python fonction with prototype: def lookup(obj):

Usage: lookup(obj)
returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
     Function that returns

     the list of available attributes and methods of an object
     Args:
        obj: python any data type object
    """
    if obj:
        return dir(obj)
