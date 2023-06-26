#!/usr/bin/python3

def safe_print_division(a, b):
    if isinstance(a, int) and isinstance(b, int):
        result = 0
        try:
            result = a / b
        except ZeroDivisionError as e:
            result = None
        finally:
            print("Inside result: {}".format(result))
        return result
