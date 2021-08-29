"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem

Task

You are given two arrays A and B. Both have dimensions of N x N.
Your task is to compute their matrix product.
"""
import numpy

n = int(input())

A = []
B = []
for _ in range(n):
    line = list(map(int, input().split(' ')))
    A.append(line)
A = numpy.array(A)

for _ in range(n):
    line = list(map(int, input().split(' ')))
    B.append(line)
B = numpy.array(B)

print(numpy.dot(A, B))
