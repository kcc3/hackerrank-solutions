def equalize_array(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem

    Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the
    minimum number of elements to delete to reach his goal.

    For example, if his array is arr = [1, 2, 2, 3], we see that he can delete the 2 elements 1 and 3 leaving
    arr = [2, 2]. He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The
    minimum number of deletions is 2.

    Args:
        arr (list): list of integers

    Returns:
        int: the minimum number of elements to delete for all elements in the array to be equal
    """
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    high_count = max(counts.iteritems(), key=lambda x: x[1])
    return len(arr) - high_count[1]


if __name__ == "__main__":
    print equalize_array([1, 2, 2, 3])
    print equalize_array([1, 2, 3, 1, 2, 3, 3, 3])