"""Hackerrank Problem: https://www.hackerrank.com/challenges/ginorts/problem

You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()

# Initialize lists to store the different types of characters
lower = []
upper = []
odd_digit = []
even_digit = []

# Parse through string
for letter in string:
    # 0 - 9
    if letter.isdigit():
        if int(letter) % 2:
            odd_digit.append(letter)
        else:
            even_digit.append(letter)
    # a - z
    elif letter.islower():
        lower.append(letter)
    # A - Z
    elif letter.isupper():
        upper.append(letter)

sorted_string = ''
print(sorted_string.join(sorted(lower)) + sorted_string.join(sorted(upper)) + sorted_string.join(sorted(odd_digit)) + sorted_string.join(sorted(even_digit)))
