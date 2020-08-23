def maximum_perimeter_triangle(sticks):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

    Given an array of stick lengths, use 3 of them to construct a non-degenerate triange with the maximum possible
    perimeter. Print the lengths of its sides as 3 space-separated integers in non-decreasing order.

    If there are several valid triangles having the maximum perimeter:

    1. Choose the one with the longest maximum side.
    2. If more than one has that maximum, choose from them the one with the longest minimum side.
    3. If more than one has that maximum as well, print any one them.

    If no non-degenerate triangle exists, print -1.

    Solve:
        We sort the list, and then iterate through and check first: if the sticks create a non-degenerate triangle, and
        then whether the stick lengths create a larger perimeter than the current largest perimeter solution

    Args:
        sticks (list): Array of stick lengths

    Returns:
        list: list containing the 3 stick lengths creating the non-degenerate triangle with the maximum possible
        perimeter or -1 if not possible
    """
    sticks.sort()
    tri = [-1]
    for i in range(len(sticks)-2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            if sticks[i] + sticks[i+1] + sticks[i+2] > sum(tri):
                tri = sticks[i:i+3]
    return tri


if __name__ == "__main__":
    assert maximum_perimeter_triangle([1, 1, 1, 3, 3]) == [1, 3, 3]
    assert maximum_perimeter_triangle([3, 9, 2, 15, 3]) == [2, 3, 3]
