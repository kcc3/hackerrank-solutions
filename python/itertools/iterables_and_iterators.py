"""
Hackerrank Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""
import itertools

# Read in the inputs which consists of three lines:
# The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated
# lowercase English letters, denoting the elements of the list. The third and the last line of input contains the
# integer K, denoting the number of indices to be selected.
n = int(input())
letters = map(str, input().split(" "))
k = int(input())
# Find the probability that the letter 'a' is in at least one of the K indices
combos = list(itertools.combinations(letters, k))
count = len([i for i in combos if "a" in i])
print(count/len(combos))