"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

Task

You are given a 2-D array of size N x M
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None
"""
import numpy

n, m = map(int, input().split(' '))

array = []
for _ in range(n):
    a = list(map(int, input().split(' ')))
    array.append(a)

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))
