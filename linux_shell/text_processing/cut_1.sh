#!/bin/bash
# Hackerrank Problem: https://www.hackerrank.com/challenges/text-processing-cut-1/problem
while read line
do
echo $line | cut -c 3
done
