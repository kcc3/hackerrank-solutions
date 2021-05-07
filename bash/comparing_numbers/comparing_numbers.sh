#!/bin/bash

# Hackerrank Problem: https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem

# Read in X and Y
read x
read y

# Do the compare
if [ $x -lt $y ]
    then
        echo "X is less than Y"
fi

if [ $x -eq $y ]
    then
        echo "X is equal to Y"
fi

if [ $x -gt $y ]
    then
        echo "X is greater than Y"
fi
