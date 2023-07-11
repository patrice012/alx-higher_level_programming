#!/usr/bin/python3
"""
Module contains script that adds all arguments to a Python list,
and then save them to a file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args_to_list(argv: list):
    """
    Add args to json file
    """
    if type(argv) is not list:
        raise TypeError("argv must be a list of arguments")
    filename = "add_item.json"
    try:
        data = load_from_json_file(filename)
    except FileNotFoundError as e:
        data = list()
    data.extend(argv)
    save_to_json_file(data, filename)


if __name__ == "__main__":
    from sys import argv
    add_args_to_list(argv[1:])
