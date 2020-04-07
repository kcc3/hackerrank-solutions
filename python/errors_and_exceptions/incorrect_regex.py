"""
Hackerrank Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem

You are given a string S.
Your task is to find out whether S is a valid regex or not.
"""
import re


def check_regex():
    """Function to check if the passed in string S is a valid regex or not

    Returns:
        bool: Outcome of whether string S is a valid regex or not
    """
    t = input()
    for i in xrange(t):
        s = raw_input()
        try:
            re.compile(s)
            print True
        except re.error:
            print False


if __name__ == "__main__":
    check_regex()