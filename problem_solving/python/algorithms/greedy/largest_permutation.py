def largest_permutation(k, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/largest-permutation/problem

    You are given an unordered array of unique integers incrementing from 1. You can swap any two elements a limited
    number of times. Determine the largest lexicographical value array that can be created by executing no more than the
    limited number of swaps.

    For example, if arr = [1, 2, 3, 4] and the maximum swaps k = 1, the following arrays can be formed by swapping the 1
    with the other elements:

    [2,1,3,4]
    [3,2,1,4]
    [4,2,3,1]

    The highest value of the four (including the original) is [4, 2, 3, 1]. If k >= 2, we can swap to the highest
    possible value: [4, 3, 2, 1].

    Solve:
        We store the values in a dictionary so we can access the position of each value in O(1) speed.  We then iterate
        through the list starting at the highest value, and swap it IF it isn't already in the correct position. We then
        update the dictionary with the swapped values, and then proceed to the next value to swap.

    Args:
        k (int): Number of swaps to perform
        arr (list): List of numbers where 1 <= arr[i] <= n

    Returns:
        list containing the largest lexicographical value array after k swaps
    """
    sorted_array = sorted(arr, reverse=True)
    vals = {v: idx for idx, v in enumerate(arr)}
    c = 0
    m = len(arr)
    while k > 0 and c < len(arr):
        if arr[c] != sorted_array[c]:
            # Swap the current highest value
            swap = arr[c]
            arr[c] = m
            arr[vals[m]] = swap
            # Update dictionary
            prev = vals[m]
            vals[m] = c
            vals[swap] = prev
            k -= 1
        m -= 1
        c += 1
    return arr


if __name__ == "__main__":
    print(largest_permutation(1, [4, 2, 3, 5, 1]))
    print(largest_permutation(2, [4, 2, 3, 5, 1]))
    print(largest_permutation(2, [4, 3, 2, 5, 1]))
    print(largest_permutation(1, [2, 1, 3]))
    print(largest_permutation(1, [2, 1]))
