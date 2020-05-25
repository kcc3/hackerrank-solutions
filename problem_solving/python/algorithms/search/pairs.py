def pairs(k, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/pairs/problem

    You will be given an array of integers and a target value. Determine the number of pairs of array elements that
    have a difference equal to a target value.

    Args:
        k (int): The target difference
        arr (list): list of integers

    Returns:
        int: number of pairs of integers whose difference is k
    """
    vals = {i: 1 for i in arr}
    count = 0
    for i in arr:
        try:
            count += vals[i + k]
        except KeyError:
            pass
    return count


if __name__ == "__main__":
    assert pairs(2, [1, 5, 3, 4, 2]) == 3
