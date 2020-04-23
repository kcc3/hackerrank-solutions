import math


def squares(a, b):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem

    Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value describing a range of
    integers. Sherlock must determine the number of square integers within that range, inclusive of the endpoints.

    Note: A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25.

    For example, the range is a = 24 and b = 49, inclusive. There are three square integers in the range: 25, 36 and 49.

    Solve: Iterate through the list, using square root and then casting as an int to essential floor the starting integer,
    and then use a ceiling value in the range.  We add 0.5 so that perfect squares as the upper move up the ceiling value,
    so for example, 9 would be 9.5, which then means the ceiling becomes 4, not 3, for the xrange function.

    Args:
        a (int): lower bound integer to check
        b (int): upper bound integer to check

    Returns:
        int: number of integers between a and b that are perfect squares
    """
    square_count = 0
    for i in xrange(int(math.sqrt(a)), int(math.ceil(math.sqrt(b+.5)))):
        if a <= i**2 <= b:
            square_count += 1
    return square_count


if __name__ == "__main__":
    print squares(3, 9)
    print squares(17, 24)
    print squares(35, 70)
    print squares(100, 1000)