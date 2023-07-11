#!/usr/bin/python3
"""
Module contains one function
Prototype: def append_write(filename="", text=""):
"""


def append_write(filename="", text=""):
    """
    Write a string to a text file (UTF8)

    Note:
    Appends a string at the end of a text file (UTF8)
    Returns the number of characters added
    Args:
        filename: text file name
        text: input text
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters
