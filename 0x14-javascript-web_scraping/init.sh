#!/usr/bin/env bash

find . -type f -name "*.js" -exec chmod +x {} \;

semistandard .

semistandard --fix