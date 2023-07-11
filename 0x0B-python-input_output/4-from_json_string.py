#!/usr/bin/python3
"""from_json_string function"""
import json


def from_json_string(my_str):
    """converts `my_str` json string into a python object"""
    return json.loads(my_str)
