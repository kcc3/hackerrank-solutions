"""Hackerrank Problem: https://www.hackerrank.com/challenges/simple-text-editor/problem

In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, S. You must
perform Q operations of the following 4 types:

1. append (W) - Append string W to the end of S.
2. delete (k) - Delete the last kth characters of S.
3. print (k) - Print the kth character of S.
4. undo () - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior
to that operation.
"""
# Read in total number of commands
num_commands = int(input())
# Setup string and command stack to track the calls and manage undos
s = ""
calls = []
# Iterate through the commands
for _ in range(num_commands):
    command = input().split(" ")
    if command[0] == "1":
        calls.append(s)
        s += command[1]
    elif command[0] == "2":
        calls.append(s)
        s = s[0:len(s)-int(command[1])]
    elif command[0] == "3":
        print(s[int(command[1])-1])
    elif command[0] == "4":
        s = calls.pop()