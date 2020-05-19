def find_median(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/find-the-median/problem

    Return an integer that represents the median of the array.

    Args:
        arr: list of integers

    Returns:
        int: the value of the median in the array
    """
    return sorted(arr)[(len(arr)-1)//2]


if __name__ == "__main__":
    assert find_median([0, 1, 2, 4, 6, 5, 3]) == 3