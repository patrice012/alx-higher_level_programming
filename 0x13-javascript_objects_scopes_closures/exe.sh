#!/usr/bin/bash

# check code style
semistandard .

# make all JavaScript files executable
find . -type f -name "*.js" -exec chmod +x {} \;