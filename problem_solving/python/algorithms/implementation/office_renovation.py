def get_max_area(w, h, boundaryType, boundaryDist):
    """Office Renovation Hackerrank Problem

    Args:
        w (int): Width of the office
        h (int): Height of the office
        boundaryType (list): List containing 0 or 1 based on whether we're working with horizontal or vertical carpet
        boundaryDist (list): List containing the distance that the carpet is being renovated

    Returns:
        list: List of the maximum area remaining for the workers
    """
    box = [[0, 0], [w, h]]
    results = []
    for i in range(len(boundaryType)):
        # Horizontal
        if boundaryType[i] == 0:
            top = h - boundaryDist[i]
            bottom = boundaryDist[i]
            # Now, see how we are slicing the box, if we're using the bottom half or top half, and
            # Calculate the coorindates of the new box
            if max(bottom, top) == bottom:
                box[1][1] = max(bottom, top)
            elif max(bottom, top) == top:
                box[0][1] = min(bottom, top)
            # Append the new area
            results.append((box[1][1] - box[0][1]) * (box[1][0] - box[0][0]))

        # Vertical
        if boundaryType[i] == 1:
            left = boundaryDist[i]
            right = w - boundaryDist[i]
            # Now, see how we are slicing the box, if we're using the left half or right half, and
            # Calculate the coorindates of the new box
            if max(left, right) == left:
                box[1][0] = max(left, right)
            elif max(left, right) == right:
                box[0][0] = min(left, right)
            # Append the new area
            results.append((box[1][1] - box[0][1]) * (box[1][0] - box[0][0]))
    return results


if __name__ == "__main__":
    # print(get_max_area(2, 2, [0, 1], [1, 1]))
    # print(get_max_area(4, 3, [1, 1], [1, 3]))
    print(get_max_area(4, 4, [0, 1], [3, 1]))