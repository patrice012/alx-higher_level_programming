#!/bin/bash
betty *.c

betty *.h

pycodestyle --first *.py
