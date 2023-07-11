#!/usr/bin/python3
"""
Module contains one function
Prototype: def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)

    Note:
    function should overwrite the content of the file if it already exists
    Returns the number of characters written:
    Args:
        filename: text file name
        text: input text
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters
