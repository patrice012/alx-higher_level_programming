#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            temp += chr(ord(i) - 32)
            continue
        temp += i
    print("{:s}".format(temp))
