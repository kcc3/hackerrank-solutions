"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-array-mathematics/problem

Task

You are given two integer arrays, A and B of dimensions N x M.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)
"""
import numpy

n, m = map(int, input().split(' '))

A = numpy.zeros((n, m), dtype=int)
B = numpy.zeros((n, m), dtype=int)

for i in range(n):
    A[i] = numpy.array([input().split(' ')], dtype=int)
for i in range(n):
    B[i] = numpy.array([input().split(' ')], dtype=int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
