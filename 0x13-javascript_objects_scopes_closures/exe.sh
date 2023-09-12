#!/usr/bin/bash

# check code style
semistandard .

# auto fix some error
semistandard --fix

# make all JavaScript files executable
find . -type f -name "*.js" -exec chmod +x {} \;