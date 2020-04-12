"""
Hackerrank Problem: https://www.hackerrank.com/challenges/zipped/problem
"""
# Read in the input values for how many lines to read
n, x = map(int, input().split(" "))
scores = []
# Iterate through inputs and get the number of scores
for i in range(x):
    input_scores = list(map(float, input().split(" ")))
    scores.append(input_scores)
# Get the scores for each student by zipping the score inputs
averages = zip(*scores)
# Print out average score for each student
for score in averages:
    print(sum(score)/len(scores))
