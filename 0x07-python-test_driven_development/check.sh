#!/bin/bash

echo "============  start task 0 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
echo "function docstings count:"
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
echo "================================================"

echo "============  start task 1 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("2-matrix_divided").__doc__)' | wc -l
echo "function docstings count:"
python3 -c 'print(__import__("2-matrix_divided").matrix_divided.__doc__)' | wc -l
echo "================================================"

