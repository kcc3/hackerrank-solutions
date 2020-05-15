def counting_sort(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/countingsort2/problem

    Given an unsorted list of integers, use the counting sort method to sort the list and then print the sorted list.

    Args:
        arr (list): List of integers to sort

    Returns:
        list: The list of integers in sorted ascending order
    """
    sorted_list = []
    counted_list = [0] * 100
    for i in arr:
        counted_list[i] += 1
    for idx, num in enumerate(counted_list):
        for _ in range(num):
            sorted_list.append(idx)
    return sorted_list


if __name__ == "__main__":
    print(counting_sort([1, 1, 3, 2, 1]))