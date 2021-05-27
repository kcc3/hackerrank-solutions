#!/bin/bash
# Hackerrank Problem: https://www.hackerrank.com/challenges/text-processing-cut-4/problem
while read line
do
echo $line | cut -c 0-4
done
