def stones(n, a, b):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/manasa-and-stones/problem

    Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the
    trail and notices that any two consecutive stones' numbers differ by one of two values. Legend has it that there is
    a treasure trove at the end of the trail. If Manasa can guess the value of the last stone, the treasure will be hers.

    For example, assume she finds 2 stones and their differences are a = 2 or b = 3. We know she starts with a 0 stone
    not included in her count. The permutations of differences for the two stones would be [2, 2], [2, 3], [3, 2] or
    [3, 3]. Looking at each scenario, stones might have [2, 4], [2, 5], [3, 5] or [3, 6] on them. The last stone might
    have any of 4, 5, or 6 on its face.

    Compute all possible numbers that might occur on the last stone given a starting stone with a 0 on it, a number of
    additional stones found, and the possible differences between consecutive stones. Order the list ascending.

    Args:
        n (int): the number of non-zero stones found
        a (int): the first possible difference
        b (int): the other possible difference

    Returns:
        list: list of the possible values of the last stone
    """
    results = []
    for i in range(0, n):
        stone = (n - i - 1) * a + i * b
        results.append(stone)
    return sorted(set(results))


if __name__ == "__main__":
    print(stones(3, 1, 2))
    print(stones(4, 10, 100))
