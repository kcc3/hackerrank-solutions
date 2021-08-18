"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

Task

You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.
"""
import numpy

# Initialize array
array = []
# Read in the number of lines to parse
n, m = input().split(' ')

# Iterate through each line and add to the array
array = []
for _ in range(int(n)):
    line = input()
    array_map = map(int, line.split(' '))
    cur_array = numpy.array(list(array_map))
    array.append(cur_array)

# Convert array to a bumpy array and print out transpose and flatten
array = numpy.array(array)
print(numpy.transpose(array))
print(array.flatten())
