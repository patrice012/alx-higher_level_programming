#!/usr/bin/python3
"""
Module conatins one function
Prototype: def to_json_string(my_obj):
"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an objects"""
    json_data = json.dumps(my_obj)
    return json_data
