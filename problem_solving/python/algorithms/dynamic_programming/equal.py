import sys


def equal(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/equal/forum

    Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased
    towards her friends and plans to give them more than the others. One of the program managers hears of this and tells
    her to make sure everyone gets the same number.

    To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation,
    she can give 1, 2, or 5 chocolates to all but one colleague. Everyone who gets chocolate in a round receives the
    same number of pieces.

    For example, assume the starting distribution is [1, 1, 5]. She can give 2 bars to the first two and the
    distribution will be [3, 3, 5]. On the next round, she gives the same two 2 bars each, and everyone has the same
    number: [5, 5, 5].

    Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the
    same number of chocolates.

    Solution:
        For this one, instead of adding chocolates to all but one colleague, we instead solve by focusing on the fact
        that removing chocolates from one person is the same, so we can then iterate through the list and figure out
        the minimum number of steps it would take to equalize the list by removing chocolates from a colleague

    Args:
        arr: Array of integers to equalize

    Returns:
        (int): The minimum number of operations needed to equalize the array
    """
    arr.sort()
    steps = sys.maxsize
    for i in range(3):
        current_steps = 0
        for j in range(len(arr)):
            delta = arr[j] - arr[0] + i
            current_steps += delta // 5 + delta % 5 // 2 + delta % 5 % 2
        steps = min(current_steps, steps)
    return steps


if __name__ == "__main__":
    assert equal([2, 2, 3, 7]) == 2
    assert equal([10, 7, 12]) == 3
