#!/bin/bash
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base.py
python3 -m unittest tests/test_models/test_square.py
python3 -m unittest tests/test_models/test_rectangle.py
