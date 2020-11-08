def largest_rectangle(h):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/largest-rectangle/problem

    Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a
    shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

    Args:
        h (list): List of building heights

    Returns:
        (int): The largest area formed from the buildings
    """
    largest_area = 0
    # Iterate through each building in list, and then determine the area if that building is the lowest height
    for i in range(len(h)):
        num_buildings = 0
        # Compare against buildings to the left
        for left in range(i, -1, -1):
            if h[left] >= h[i]:
                num_buildings += 1
            else:
                break
        # Compare buildings to the right
        for right in range(i + 1, len(h)):
            if h[right] >= h[i]:
                num_buildings += 1
            else:
                break
        # Next, calculate the area formed by this building and it's neighbors
        area = h[i] * num_buildings
        # Set as largest new area if it's the current largest
        if area > largest_area:
            largest_area = area
    return largest_area


if __name__ == "__main__":
    assert largest_rectangle([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]) == 26152
    assert largest_rectangle([6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494]) == 18060
