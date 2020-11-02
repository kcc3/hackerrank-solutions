"""Hackerrank Problem: https://www.hackerrank.com/challenges/equal-stacks/problem

You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can
change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you
must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height,
then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.
"""

import math
import os
import random
import re
import sys


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def equal_stacks(h1, h2, h3):
    """Compare three stacks of cylinders and return the maximum possible height of the stacks such that all of the
    stacks are exactly the same height

    Solve:
        For this, we can use a dictionary, and store the "heights" of the stacks as the key with the value being a list
        that the stack will append to as we iterate through each possible sum for each stack.  By doing this, we can then
        simply look for the height key that has a list of length 3, as that will be the highest maximum sum

    Args:
        h1 (list): list of integers in stack 1
        h2 (list): list of integers in stack 2
        h3 (list): list of integers in stack 3

    Returns:
        (int): The maximum possible height of the stacks where all have the same height
    """
    sums = {}
    s = 0
    for i in reversed(h1):
        s += i
        sums[s] = [1]
    s = 0
    for i in reversed(h2):
        s += i
        if s in sums:
            sums[s].append(1)
    s = 0
    for i in reversed(h3):
        s += i
        if s in sums:
            sums[s].append(1)
    largest = 0
    for i in sums:
        if len(sums[i]) == 3 and i > largest:
            largest = i
    return largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equal_stacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
