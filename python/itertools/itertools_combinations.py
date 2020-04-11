"""
Hackerrank Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

Task
----
You are given a string s.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format
----
A single line containing the string s and integer value k separated by a space.
"""
import itertools


def main():
    s, k = raw_input().split(" ")
    for i in xrange(1, int(k)+1):
        combinations = list(itertools.combinations(sorted(s), i))
        for combo in sorted(combinations):
            print "".join(combo)


if __name__ == "__main__":
    main()