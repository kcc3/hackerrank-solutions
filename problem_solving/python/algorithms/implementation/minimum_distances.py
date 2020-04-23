def minimum_distances(a):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/minimum-distances/problem

    We define the distance between two array values as the number of indices between the two values. Given a, find the
    minimum distance between any pair of equal elements in the array. If no such value exists, print -1.

    Args:
        a (list): list of integers to check

    Returns:
        int: the minimum distance between any pair of equal elements, or -1
    """
    if len(set(a)) == len(a):
        return -1
    smallest_distance = len(a)
    values = {}
    for idx, val in enumerate(a):
        if val in values:
            distance = idx - values[val]
            if distance < smallest_distance:
                smallest_distance = distance
        values[val] = idx
    return smallest_distance


if __name__ == "__main__":
    print minimum_distances([7, 1, 3, 4, 1, 7])