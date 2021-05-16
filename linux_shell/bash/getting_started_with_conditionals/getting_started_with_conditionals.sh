#!/bin/bash

# Hackerrank Problem: https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem

# Read in character
read c

# Do the compare
if [ $c = "Y" ] || [ $c = "y" ]
    then
        echo "YES"
fi

if [ $c = "N" ] || [ $c = "n" ]
    then
        echo "NO"
fi
