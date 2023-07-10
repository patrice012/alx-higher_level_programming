#!/usr/bin/python3
"""
Define Python fonction with prototype: def lookup(obj):

Usage: lookup(obj)
returns the list of available attributes and methods of an object
"""


def lookup(obj):
    if obj:
        return dir(obj)
