def surface_area(A):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/3d-surface-area/problem

    Madison, is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory. Mason has a
    2D board A of size H x W with H rows and W columns. The board is divided into cells of size 1 x 1 with each cell
    indicated by it's coordinate (i, j). The cell (i, j) has an integer Aij written on it. To create the toy Mason
    stacks Aij number of cubes of size 1 x 1 x 1 on the cell (i, j).

    Given the description of the board showing the values of Aij and that the price of the toy is equal to the 3d
    surface area find the price of the toy.

    Args:
        A (list): 2D array representing the height of the toy

    Returns:
        int: The total surface area represented as an integer
    """
    w = len(A)
    h = len(A[0])
    # Add a layer of 0's around the outside of the grid
    grid = []
    for i in range(w+2):
        row = []
        for j in range(h+2):
            if i == 0 or i == w+1:
                row.append(0)
            elif j == 0 or j == h+1:
                row.append(0)
            else:
                row.append(A[i-1][j-1])
        grid.append(row)

    # Add the top and bottom surface area as that's always part of the surface area
    surf_area = w * h * 2
    for i in range(1, w+1):
        for j in range(1, h+1):
            print(i, j)
            surf_area += max(0, grid[i][j] - grid[i][j-1])
            surf_area += max(0, grid[i][j] - grid[i][j+1])
            surf_area += max(0, grid[i][j] - grid[i-1][j])
            surf_area += max(0, grid[i][j] - grid[i+1][j])

    return surf_area


if __name__ == "__main__":
    area = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
    print(surface_area(area))

    area2 = [[1]]
    print(surface_area(area2))