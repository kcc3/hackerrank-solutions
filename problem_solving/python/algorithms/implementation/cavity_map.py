def cavity_map(grid):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/cavity-map/problem

    You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
    We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell
    adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.

    Find all the cavities on the map and replace their depths with the uppercase character X.

    For example, given a matrix:

    989
    191
    111

    You should return:

    989
    1X1
    111

    The center cell was deeper than those on its edges: [8,1,1,1]. The deep cells in the top two corners don't share an
    edge with the center cell.

    Args:
        grid (list): a list of strings denoting the depths of the teeth

    Returns:
        list: a list of strings with X's in the place where there are cavities
    """
    output_grid = grid
    n = len(grid)
    for i in xrange(n):
        for j in xrange(n):
            if 0 < i < (n - 1) and 0 < j < (n - 1):
                if grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i-1][j]:
                    if grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1]:
                        output_grid[i] = output_grid[i][:j] + "X" + output_grid[i][j+1:]
    return output_grid


if __name__ == "__main__":
    map = ["1112", "1912", "1892", "1234"]
    print cavity_map(map)