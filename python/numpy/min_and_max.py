"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-min-and-max/problem

Task

You are given a 2-D array with dimensions N x M.
Your task is to perform the min function over axis 1 and then find the max of that.
"""
import numpy

n, m = map(int, input().split(' '))

array = []
for _ in range(n):
    a = list(map(int, input().split(' ')))
    array.append(a)

min_array = numpy.min(array, axis=1)
print(max(min_array))
