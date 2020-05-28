def balanced_sums(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/sherlock-and-array/problem

    Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of
    all elements to the left is equal to the sum of all elements to the right. For instance, given the array ,
     arr = [5, 6, 8, 11], 8 is between two subarrays that sum to 11. If your starting array is [1], that element 
     satisfies the rule as left and right sum to 0.

    You will be given arrays of integers and must determine whether there is an element that meets the criterion.

    Args:
        arr (list): An array of integers

    Returns:
        str: YES or NO depending on whether there is a balanced sum in the list
    """
    left = 0
    right = sum(arr)
    for i in range(len(arr)):
        right -= arr[i]
        if left == right:
            return "YES"
        left += arr[i]
    return "NO"


if __name__ == "__main__":
    print(balanced_sums([1, 2, 3]))
    print(balanced_sums([1, 2, 3, 3]))
