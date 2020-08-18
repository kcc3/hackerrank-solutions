def maximizing_xor(l, r):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/maximizing-xor/problem

    Given two integers, l and r, find the maximal value of a xor b, written a @ b, where a and b satisfy the following
    condition:

    l <= a <= b <= r

    Solve:
        We XOR the l and r bound and find the length of that integer in binary form. That gives us the binary from which
        we can create the highest value of a xor b, because that falls within l and r.

    Args:
        l (int): an integer, the lower bound inclusive
        r (int): an integer, the upper bound inclusive

    Returns:
        int: maximum value of the xor operations for all permutations of the integers from l to r inclusive
    """
    xor = l ^ r
    xor_binary = "{0:b}".format(xor)
    return pow(2, len(xor_binary)) - 1


if __name__ == "__main__":
    print(maximizing_xor(10, 15))
    print(maximizing_xor(11, 100))
