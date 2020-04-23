def circular_array_rotation(a, k, queries):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem

    John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation
    moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's
    abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number
    of times then determine the value of the element at a given position.

    For each array, perform a number of right circular rotations and return the value of the element at a given index.

    For example, array a = [3, 4, 5], number of rotations, k = 2 and indices to check, m = [1, 2].
    First we perform the two rotations:
    [3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]

    Now return the values from the zero-based indices  and  as indicated in the  array.

    a[1] = 5
    a[2] = 3

    Args:
        a (list): array of integers to rotate
        k (int): the number of times to shift the array right
        queries (list): list of indices to query on the newly shifted array

    Returns:
        list: a list of values returned from the queries
    """
    query_values = []
    for query in queries:
        query_values.append(a[(query-k) % len(a)])
    return query_values


if __name__ == "__main__":
    a = [1, 2, 3]
    k = 2
    q = [0, 1, 2]
    print circular_array_rotation(a, k, q)