"""
Hackerrank Problem: https://www.hackerrank.com/challenges/any-or-all/problem

Given a space separated list of integers, check to see if all the integers are positive, and if so, check if any integer
is a palindromic integer.
"""
n = int(input())
ints = list(input().split(" "))
# Check to see if all integers in the list are positive
if all(int(i) >= 0 for i in ints):
    # Check if any of the integers are a palindrome - where the digit number is the same if digits are reversed
    print(any(j == j[-1] for j in ints))
else:
    print(False)