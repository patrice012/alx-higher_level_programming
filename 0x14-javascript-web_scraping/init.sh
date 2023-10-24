#!/usr/bin/env bash

find . -type f -name "*.js" -exec black {} \;

semistandard .

semistandard --fix