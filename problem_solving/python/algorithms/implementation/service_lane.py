def service_lane(widths, cases):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/service-lane/problem

    Calvin is driving his favorite vehicle on the 101 freeway. He notices that the check engine light of his vehicle is
    on, and he wants to service it immediately to avoid any risks. Luckily, a service lane runs parallel to the highway.
    The service lane varies in width along its length.

    You will be given an array of widths at points along the road (indices), then a list of the indices of entry and
    exit points. Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that
    segment of the service lane safely.

    For example, there are n = 4 measurements yielding width = [2, 3, 2, 1]. If our entry index, i = 1 and our exit,
    j = 2, there are two segment widths of 2 and 3 respectively. The widest vehicle that can fit through both is 2.
    If i = 2 and j = 4, our widths are [3, 2, 1] which limits vehicle width to 1.

    Solve: For each case, find the min of the values using list slicing

    Args:
        widths (list): list representing the highway service road widths
        cases (list): a two dimensional array of integers where each element is an array of two integers representing
            starting and ending indices for a segment to consider .

    Returns:
        list: list of the widest vehicle that can fit in the service road based on the passed in cases and road widths
    """
    widest_vehicle = []
    for case in cases:
        widest_vehicle.append(min(widths[case[0]:case[1]+1]))
    return widest_vehicle


if __name__ == "__main__":
    widths_test = [2, 3, 1, 2, 3, 2, 3, 3]
    cases_test = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
    print service_lane(widths_test, cases_test)