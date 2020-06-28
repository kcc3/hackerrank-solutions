def two_arrays(k, A, B):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/two-arrays/problem

    Consider two n-element arrays of integers, A = [A[0], A[1], ...., A[n-1]] and B = [B[0], B[1], ..., B[n-1]]. You
    want to permute them into some A' and B' such that the relation A'[i] + B'[i] >= k holds for all i where 0 <= i < n.
    For example, if A = [0, 1], B = [0, 2], and k = 1, a valid A', B' satisfying our relation would be A' = [1, 0] and
    B' = [0, 2], 1 + 0 >= 1 and 0 + 2 >= 1.

    You are given q queries consisting of A, B, and k. For each query, print YES on a new line if some permutation A',
    B' satisfying the relation above exists. Otherwise, print NO.

    Solve:
        We sort the two arrays, A in ascending order, and B in descending order, so we can iterate through once and
        compare each position i to see if A[i] + B[i] is greater or equal to k.

    Args:
        k (int): an integer
        A (list): first array of integers
        B (list): second array of integers

    Returns:
        str: "YES" or "NO" depending on whether we can find permutation A', B' that satisfy the relationship
    """
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    print(two_arrays(10, [2, 1, 3], [7, 8, 9]))