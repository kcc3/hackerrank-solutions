def athlete_sort(spreadsheet, k):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem

    You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and
    so on). You are required to sort the data based on the Kth attribute and print the final resulting table

    Args:
        spreadsheet (list): Spreadsheet list of athletes and their details
        k (int): the specified attribute to sort by

    Returns:
        None
    """
    sorted_sheet = {}
    for i in spreadsheet:
        if i[k] not in sorted_sheet.keys():
            sorted_sheet[i[k]] = [i]
        else:
            sorted_sheet[i[k]].append(i)
    for i in sorted(sorted_sheet.keys()):
        for j in sorted_sheet[i]:
            print(" ".join(str(k) for k in j))


if __name__ == "__main__":
    test_arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
    k = 1
    athlete_sort(test_arr, k)