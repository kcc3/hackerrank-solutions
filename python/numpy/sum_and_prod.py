"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

Task

You are given a 2-D array with dimensions N x M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.
"""
import numpy

n, m = map(int, input().split(' '))

array = []
for _ in range(n):
    a = list(map(int, input().split(' ')))
    array.append(a)

print(numpy.prod(numpy.sum(array, axis=0), axis=0))
