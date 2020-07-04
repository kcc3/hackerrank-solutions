def max_min(k, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/angry-children/problem

    You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements
    of arr such that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as

    max(subarr) - min(subarr)

    Where:
    - max denotes the largest integer in subarr
    - min denotes the smallest integer in subarr

    Args:
        k (int): the number of elements in the array to create
        arr (list): an array of integers

    Returns:
        int: integer that denotes the minimum possible value of unfairness
    """
    arr.sort()
    left = 0
    right = k - 1
    mm = arr[len(arr)-1]
    while right <= len(arr)-1:
        if arr[right] - arr[left] < mm:
            mm = arr[right] - arr[left]
            if mm == 0:
                break
        # Slide window one position and check again
        left += 1
        right += 1
    return mm


if __name__ == "__main__":
    print(max_min(3, [10, 100, 300, 200, 1000, 20, 30]))
    print(max_min(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
    print(max_min(2, [1, 2, 1, 2, 1]))
