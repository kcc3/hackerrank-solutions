"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-polynomials/problem

Task

You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
"""
import numpy

P = numpy.array(list(map(float, input().split(' '))))
x = int(input())
print(numpy.polyval(P, x))
