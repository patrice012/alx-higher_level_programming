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

echo "============  start task 2 ===================="
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

echo "============  start task 3 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("3-say_my_name").__doc__)' | wc -l
echo "function docstings count:"
python3 -c 'print(__import__("3-say_my_name").say_my_name.__doc__)' | wc -l
echo "================================================"


echo "============  start task 4 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/4-print_square.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("4-print_square").__doc__)' | wc -l
echo "function docstings count:"
python3 -c 'print(__import__("4-print_square").print_square.__doc__)' | wc -l
echo "================================================"


echo "============  start task 5 ===================="
echo "Testint started..."
echo ""
python3 -m doctest -v ./tests/5-text_indentation.txt | tail -2
echo "Testing ended..."
echo ""
echo "Module docstings count:"
python3 -c 'print(__import__("5-text_indentation").__doc__)' | wc -l
echo "function docstings count:"
python3 -c 'print(__import__("5-text_indentation").text_indentation.__doc__)' | wc -l
echo "================================================"


echo "============  start task 6 ===================="
echo "Testint started..."
echo ""
python3 -m unittest tests.6-max_integer_test | tail -1
echo "Testing ended..."
echo "================================================"
