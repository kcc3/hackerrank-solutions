def grid_challenge(grid):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/grid-challenge/problem

    Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending.
    Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if
    they are not.

    For example, given:

    a b c
    a d e
    e f g

    The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so
    the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

    Args:
        grid (array): Array of strings

    Returns:
        str: "YES" or "NO" if columns of grid are in ascending order after sorting the rows
    """
    # First sort the rows
    for i, s in enumerate(grid):
        grid[i] = "".join(sorted(s))
    prev = "a"
    # Now, check the columns and see if string is in ascending order
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if prev > grid[j][i]:
                return "NO"
            prev = grid[j][i]
        prev = "a"
    return "YES"


if __name__ == "__main__":
    assert grid_challenge(['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']) == "YES"
    assert grid_challenge(["mpxz", "abcd", "wlmf"]) == "NO"
