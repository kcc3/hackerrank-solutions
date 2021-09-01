"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-linear-algebra/problem

Task

You are given a square matrix A with dimensions N x N. Your task is to find the determinant.
Note: Round the answer to 2 places after the decimal.
"""
import numpy

N = int(input())

A = []
for i in range(N):
    line = list(map(float, input().split(' ')))
    A.append(line)
A = numpy.array(A)

print(round(numpy.linalg.det(A), 2))
