def closest_numbers(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/closest-numbers/problem

    Determine which pair or pairs of elements have the smallest absolute difference between them.

    Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between
    them. If there are multiple pairs, find them all.

    Args:
        arr: List of integers

    Returns:
        list: list of pairs of integers that have the absolute smallest difference between them
    """
    diffs = {}
    arr.sort()
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff in diffs:
            diffs[diff].extend([arr[i], arr[i+1]])
        else:
            diffs[diff] = [arr[i], arr[i+1]]
    return diffs[sorted(diffs.keys())[0]]


if __name__ == "__main__":
    print(closest_numbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))