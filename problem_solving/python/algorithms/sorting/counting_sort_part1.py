def counting_sort(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/countingsort1/problem

    Alternative Sorting Method to Comparison Sorting:
    Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose
    index range covers the entire range of values in your array to sort. Each time a value occurs in the original array,
    you increment the counter at that index. At the end, run through your counting array, printing the value of each
    non-zero valued index that number of times.

    Args:
        arr (list): List of integers to count and sort

    Returns:
        list: List of the number of occurrences of each integer with arr[idx] = occurrences of that idx value
    """
    counted_list = [0] * 100
    for i in arr:
        counted_list[i] += 1
    return counted_list


if __name__ == "__main__":
    print(counting_sort([1, 1, 3, 2, 1]))