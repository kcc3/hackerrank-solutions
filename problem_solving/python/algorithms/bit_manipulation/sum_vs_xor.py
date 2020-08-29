def sum_xor(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/sum-vs-xor/problem

    Given an integer n, find each x such that:

    0 <= x <= n
    n + x = n ^ x

    Solve:
        We count the number of zeros that are in the binary representation of the integer, because for sum and xor to be
        equal, it occurs when there are 0s in the digit where an XOR would return a 1, and an addition would return a 1
        as well.  For example: for the integer "10", which is binary "1010", if you add or XOR 1, you would end up with
        "1011" for both, because of the least significant 0 being flipped to a 1. We then return the total combinations
        of these values, which is 2^(number of zeros)

    Args:
        n (int): Integer to check

    Returns:
        int: The total number of integers that satisfy the sum = xor problem
    """
    if n == 0:
        return 1
    bin = "{0:b}".format(n)
    zeros = bin.count("0")
    return pow(2, zeros)


if __name__ == "__main__":
    assert sum_xor(5) == 2
    assert sum_xor(10) == 4
    assert sum_xor(0) == 1
