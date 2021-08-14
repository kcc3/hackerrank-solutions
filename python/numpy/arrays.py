"""Hackerrank Problem: https://www.hackerrank.com/challenges/np-arrays/problem"""
import numpy


def arrays(arr):
    """Turn a space separated list of numbers into an array and return the reversed version of array

    Args:
        arr (str): Space separated list of numbers

    Returns:
        (numpy.array): Reversed numpy array
    """
    a = numpy.array(arr, float)
    return numpy.flip(a)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
