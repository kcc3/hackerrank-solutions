"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem

Task

You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.
"""
import numpy

# Read in input
line = input()
# Convert string list into integers
array_map = map(int, line.split(' '))
array = numpy.array(list(array_map))
# Reshape array and print out result
print(numpy.reshape(array, (3, 3)))
