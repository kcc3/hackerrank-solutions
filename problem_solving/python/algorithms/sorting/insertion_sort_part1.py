def insertion_sort1(n, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/insertionsort1/problem

    Part one of explaining insertion sort, using code to show output of the list as we're pushing elements back

    Args:
        n (int): Size of the array being passed in to sort
        arr (list): The list of integers with the last element being out of order

    Returns:
        None: Does not return any data but prints out the status of the array as we are pushing elements back to sort
    """
    val = arr[(len(arr)-1)]
    done = False
    for i in reversed(range(1, len(arr))):
        if arr[i-1] > val:
            arr[i] = arr[i-1]
        else:
            arr[i] = val
            done = True
        print(" ".join(map(str, arr)))
        if done:
            break
    if arr[0] > val:
        arr[0] = val
        print(" ".join(map(str, arr)))


if __name__ == "__main__":
    # insertion_sort1(5, [2, 4, 6, 8, 3])
    # insertion_sort1(14, [1, 3, 5, 9, 13, 22, 27, 35, 46, 51, 55, 83, 87, 23])
    insertion_sort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])