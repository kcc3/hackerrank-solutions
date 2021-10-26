"""Hackerrank Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
"""
import re

# Read in string to match
input_string = input()

# Match requiring a consonant, and then multiple vowels, and ending with a consonant
match = re.findall('(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input_string)

# Print the matched substrings or -1 if none were found
if match:
    for m in match:
        print(m)
else:
    print(-1)
