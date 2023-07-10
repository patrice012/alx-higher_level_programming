#!/usr/bin/python3
"""
Module contains: MyList class
"""


class MyInt(int):
    """
    MyInt that inherits from Int
    """

    def __init__(self, num):
        self.num = num

    def __eq__(self, value):
        return self.num != value

    def __ne__(self, value):
        return self.num == value

    def __str__(self):
        return str(self.num)
