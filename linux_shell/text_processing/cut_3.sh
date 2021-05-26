#!/bin/bash
# Hackerrank Problem: https://www.hackerrank.com/challenges/text-processing-cut-3/problem
while read line
do
echo $line | cut -c 2-7
done
