#!/bin/bash
# Hackerrank Problem: https://www.hackerrank.com/challenges/text-processing-cut-5/problem
while read line
do
echo "$line" | cut -f1-3
done
