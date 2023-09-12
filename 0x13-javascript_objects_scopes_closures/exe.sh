#!/usr/bin/bash

# check code style in the current directory
semistandard .

# auto fix some error
semistandard --fix

# make all JavaScript files executable
find . -type f -name "*.js" -exec chmod +x {} \;