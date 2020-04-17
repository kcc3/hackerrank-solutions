"""
Hackerrank Problem: https://www.hackerrank.com/challenges/compress-the-string/problem

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive
occurrences of the character 'c' with (X, c) in the string.
"""
from itertools import groupby

string = input()
output = ""
for i, k in groupby(string):
    output += "({0}, {1}) ".format(len(list(k)), i)
print(output)