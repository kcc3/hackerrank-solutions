"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

Task

You are given the shape of the array in the form of space-separated integers, each integer representing the size of
different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros
and numpy.ones.
"""
import numpy

# Read in the number of lines to parse
dimensions = list(map(int, input().split(' ')))

# Convert array to a bumpy array and print out transpose and flatten
print(numpy.zeros(dimensions, dtype=numpy.int32))
print(numpy.ones(dimensions, dtype=numpy.int32))
