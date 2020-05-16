def count_sort(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/countingsort4/problem

    In this challenge you need to print the string that accompanies each integer in a list sorted by the integers. If
    two strings are associated with the same integer, they must be printed in their original order so your sorting
    algorithm should be stable. There is one other twist. The first half of the strings encountered in the inputs are to
    be replaced with the character "-" (dash).

    Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not
    since it scrambles around elements while sorting.

    In this challenge, you will use counting sort to sort a list while keeping the order of the strings preserved.

    Args:
        arr: list containing x[i] and s[i], the integers (as strings) with their associated strings

    Returns:
        None: Prints out the message after sorting and with the added dashes
    """
    total = len(arr)
    sorted_list = [[] for _ in range(total)]
    for idx, pair in enumerate(arr):
        if idx < total / 2:
            sorted_list[int(pair[0])].append("-")
        else:
            sorted_list[int(pair[0])].append(pair[1])
    message = ""
    for a in sorted_list:
        for s in a:
            message += s + " "
    print(message)


if __name__ == "__main__":
    array_data = [["0", "ab"], ["6", "cd"], ["0", "ef"], ["6", "gh"], ["4", "ij"],
                  ["0", "ab"], ["6", "cd"], ["0", "ef"], ["6", "gh"], ["0", "ij"],
                  ["4", "that"], ["3", "be"], ["0", "to"], ["1", "be"], ["5", "question"],
                  ["1", "or"], ["2", "not"], ["4", "is"], ["2", "to"], ["4", "the"]]
    count_sort(array_data)