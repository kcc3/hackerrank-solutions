"""Hackerrank Problem: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check
whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""

import re

# Read in number of inputs
number_of_tests = input()

# Iterate through each number and see if it's a valid phone number
for _ in range(int(number_of_tests)):
    number = input()
    match = re.match('[7-9][0-9]{9}$', number)
    if match:
        print('YES')
    else:
        print('NO')
