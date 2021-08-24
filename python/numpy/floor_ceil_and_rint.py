"""Hackerrank Problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

Task
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.
"""
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(input().split(' '), float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
