#!/usr/bin/bash


# format python code
find . -type f -name "*.py" -exec black  {} \;

# check for code style
find . -type f -name "*.py" -exec pycodestyle {} \;

# make executables
find . -type f -name "*.py" -exec chmod +x {} \;
find . -type f -name "*.sql" -exec chmod +x {} \;