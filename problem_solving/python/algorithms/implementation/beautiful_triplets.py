def beautiful_triplets(d, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/beautiful-triplets/problem

    Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:

    i < j < k
    a[j] - a[i] = a[k] - [j] = d

    Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence.

    For example, the sequence arr = [2, 2, 3, 4, 5] and d = 1. There are three beautiful triplets, by index:
    [i, j, k] = [0, 2, 3], [1, 2, 3], [2, 3, 4]. To test the first triplet, arr[j] - arr[i] = 3 - 2 = 1 and
    arr[k] = arr[j] = 4 - 3 = 1.

    Solve: Brute force solve can go through the array multiple times to find arr[k] - arr[j] = arr[j] - arr[i]:

    triplets = 0
    for i in xrange(len(arr)):
        for j in xrange(i, len(arr)):
            if arr[j] - arr[i] == d:
                for k in xrange(j, len(arr)):
                    if arr[k] - arr[j] == d:
                        triplets += 1
    return triplets

    A more optimized solution is to go through and find arr[i] + d, and arr[i] + d + d, as that must be satisfied to
    be beautiful, and iterates through the array once.

    Args:
        d (int): an integer to match
        arr (list): an array of integers, sorted ascending

    Returns:
        int: the number of beautiful triplets found
    """
    triplets = 0
    for i in xrange(len(arr)):
        if arr[i] + d in arr and arr[i] + d + d in arr:
            triplets += 1
    return triplets


if __name__ == "__main__":
    print beautiful_triplets(1, [2, 2, 3, 4, 5])
    print beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10])