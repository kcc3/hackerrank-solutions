def minimum_absolute_difference(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

    Given an array of integers, find and print the minimum absolute difference between any two elements in the array.

    Solve:
        Sort the array, and then compare the different between each two adjacent values.  After sorting, we know that
        the minimum absolute difference has to be between two values that are stored sequentially in the list so we
        simply find the smallest difference and return that

    Args:
        arr: Array of integers to check

    Returns:
        int: The minimum absolute difference between two elements of the array
    """
    arr.sort()
    min_diff = arr[-1] - arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff


if __name__ == "__main__":
    assert minimum_absolute_difference([3, -7, 0]) == 3
    assert minimum_absolute_difference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1
    assert minimum_absolute_difference([1, -3, 71, 68, 17]) == 3
