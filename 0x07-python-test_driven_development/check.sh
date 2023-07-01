#!/bin/bash

echo "============  start task 0 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
echo "add_integer docstings count:"
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
echo "================================================"

