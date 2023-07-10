#!/usr/bin/python3
"""
Module contains: MyList class
"""


class MyList(list):
    """
    MyList that inherits from list

    add feature to a builtin List data type
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
