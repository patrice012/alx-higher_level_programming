#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set(my_list)
    _sum = 0
    for i in unique:
        _sum += i
    return _sum
