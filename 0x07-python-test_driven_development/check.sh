#!/bin/bash


python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
