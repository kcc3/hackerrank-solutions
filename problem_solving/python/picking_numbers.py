from collections import OrderedDict


def picking_numbers(a):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/picking-numbers/problem

    Given an array of integers, find and print the maximum number of integers you can select from the array such that
    the absolute difference between any two of the chosen integers is less than or equal to 1. For example, if your array
    is a = [1, 1, 2, 2, 4, 4, 5, 5, 5], you can create two subarrays meeting the criterion: [1, 1, 2, 2] and
    [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.

    Args:
        a (list): list of integers to check

    Returns:
        int: the maximum length of subarray of elements that satisfies the requirement
    """
    nums = OrderedDict()
    # We convert the list into an ordered dictionary
    for i in sorted(a):
        if i in nums.keys():
            nums[i] += 1
        else:
            nums[i] = 1
    # Iterate through the ordered dictionary to find the biggest subarray that satisfies the condition that the diff
    # between two integers is <= 1 (which are our keys now)
    prev_idx = -1
    prev_count = 0
    max_count = nums[next(iter(nums))]
    for i, c in nums.iteritems():
        if i - prev_idx <= 1:
            if max_count < prev_count + c:
                max_count = prev_count + c
        elif c > max_count:
            max_count = c
        prev_idx = i
        prev_count = c
    return max_count


if __name__ == "__main__":
    array_test_1 = [4, 6, 5, 3, 3, 1]
    print picking_numbers(array_test_1)
    array_test_2 = [66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
    print picking_numbers(array_test_2)
    array_test_3 = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5,
                    97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5,
                    97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97,
                    5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
    print picking_numbers(array_test_3)