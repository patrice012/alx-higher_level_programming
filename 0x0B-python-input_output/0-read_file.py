#!/usr/bin/python3
"""
Module contains one function
Prototype: def read_file(filename=""):
"""


def read_file(filename=""):
    """
    Reads text file (UTF8) and prints it to stdout

    Args:
        filename: text file name
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
