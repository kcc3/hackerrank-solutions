def big_sorting(unsorted):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/big-sorting/problem

    Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6 digits.
    Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of
    the sorted array on a new line.

    Solve:
        We store a dictionary where the key is the length of the integer and the value is a list of integers that fit
        that length / key.  Then, we just extend a list with each sorted sub list starting from the smallest key

    Args:
        unsorted (list): Array of unsorted integers

    Returns:
        list: the sorted list of integers
    """
    sorted_dict = {}
    for i in unsorted:
        if len(str(i)) in sorted_dict.keys():
            sorted_dict[len(str(i))].append(i)
        else:
            sorted_dict[len(str(i))] = [i]
    sorted_list = []
    for k in sorted(sorted_dict.keys()):
        sorted_list.extend(sorted(sorted_dict[k]))
    return sorted_list


if __name__ == "__main__":
    print(big_sorting([6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]))
