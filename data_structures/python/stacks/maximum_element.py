"""Hackerrank Problem: https://www.hackerrank.com/challenges/maximum-element/problem

You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Setup the list which will act as our stack
stack = [-1]
# Read in the total number of commands
num_commands = int(input())
# For each command, append, pop, or return the max value as specified. When we push to the stack, we can compare
# with the current highest value so that the stack always has the max value at the tail of the list, and because when
# we pop, we are removing the last added item, so it is either the last added value, or a copy of the last max value
# when it was added
for _ in range(num_commands):
    query = input().split(" ")
    if query[0] == "1":
        stack.append(max(int(query[1]), stack[-1]))
    elif query[0] == "2":
        stack.pop()
    elif query[0] == "3":
        print(stack[-1])
    else:
        print("Unknown command")
