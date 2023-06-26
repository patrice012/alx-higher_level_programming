#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if isinstance(my_list, list):
        count = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                try:
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
                except IndexError:
                    raise
        print()
        return count
