"""
Hackerrank Problem: https://www.hackerrank.com/challenges/exceptions/problem
"""
n = input()
for i in xrange(n):
    a, b = raw_input().split(" ")
    try:
        print int(a) / int(b)
    except ZeroDivisionError as e:
        print "Error Code: {0}".format(e)
    except ValueError as v:
        print "Error Code: {0}".format(v)