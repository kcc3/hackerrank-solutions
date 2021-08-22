"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-eye-and-identity/problem

Task

Your task is to print an array of size N x M with its main diagonal elements as 1's and 0's everywhere else.
"""
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = input().split(' ')
print(numpy.eye(int(n), int(m)))
