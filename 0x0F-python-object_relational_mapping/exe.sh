#!/usr/bin/bash
echo "select mode: 1 to enable debug, any onther number for not";
read -p ">>> " mode;

if [ $mode -eq 1 ]
then
    debug=true;
else
    debug=false;
fi

# format python code
find . -type f -name "*.py" -exec black  {} \;

# check for code style
find . -type f -name "*.py" -exec pycodestyle {} \;

# make executables
find . -type f -name "*.py" -exec chmod +x {} \;
find . -type f -name "*.sql" -exec chmod +x {} \;

if $debug
then
    clear;
    find . -type f -name "test.sh" -exec chmod +x {} \;
    ./test.sh;
fi
