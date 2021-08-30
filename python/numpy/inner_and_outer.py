"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-inner-and-outer/problem

Task

You are given two arrays: A and B.
Your task is to compute their inner and outer product.
"""
import numpy

A = numpy.array(list(map(int, input().split(' '))))
B = numpy.array(list(map(int, input().split(' '))))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
