#!/usr/bin/python2
import random
number = random.randint(-10, 10)
if number < 0:
    print(f"{number:d} is negative")
elif number > 0:
    print(f"{number:d} is positive")
else:
    print("{number:d}  is zero")
