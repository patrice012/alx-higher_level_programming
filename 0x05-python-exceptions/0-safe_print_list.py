#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list):
        count = 0
        for i in range(0, x):
            try:
                value = my_list[i]
            except IndexError:
                break
            else:
                print(value, end="")
                count += 1
        print()
        return count
