"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-concatenate/problem

Task

You are given two integer arrays of size N x P and M x P (N & M are rows, and P is the column). Your task is to
concatenate the arrays along axis 0.
"""
import numpy

n, m, p = input().split(' ')
n_array = []
m_array = []
for _ in range(int(n)):
    line = input()
    array_map = map(int, line.split(' '))
    cur_array = numpy.array(list(array_map))
    n_array.append(cur_array)

for _ in range(int(m)):
    line = input()
    array_map = map(int, line.split(' '))
    cur_array = numpy.array(list(array_map))
    m_array.append(cur_array)

print(numpy.concatenate((n_array, m_array), axis=0))
