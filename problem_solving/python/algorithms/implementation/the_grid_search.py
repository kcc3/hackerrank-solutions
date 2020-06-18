def grid_search(g, p):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/the-grid-search/problem

    Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. For example:

    Grid
    ----------
    1234567890
    0987654321
    1111111111
    1111111111
    2222222222

    Pattern
    ------
    876543
    111111
    111111

    The 2D pattern begins at the second row and the third column of the grid. The pattern is said to be present in the
    grid.

    Args:
        g (list): The grid to search, an array of strings
        p (list): The pattern to search for, an array of strings

    Returns:
        str: "YES" or "NO" depending on whether the pattern is found or not
    """
    for i in range(len(g)-len(p)+1):
        # If we find a match for the first line, store the indices to search for
        match = [x for x in range(len(g[i])) if g[i].startswith(p[0], x)]
        if match:
            # Iterate through the list of indices where the first line of the pattern matched
            for j in match:
                found = True
                # Now see if the rest of the pattern matches within the same column / index
                for k in range(1, len(p)):
                    if p[k] == g[i+k][j:j+len(p[k])]:
                        continue
                    else:
                        found = False
                        break
                if found:
                    return "YES"
    return "NO"


if __name__ == "__main__":
    g = ["7283455864", "6731158619", "8988242643", "3830589324", "2229505813", "5633845374", "6473530293", "7053106601",
         "0834282956", "4607924137"]
    p = ["9505", "3845", "3530"]
    assert grid_search(g, p) == "YES"

    g2 = ["7652157548860692421022503", "9283597467877865303553675", "4160389485250089289309493", "2583470721457150497569300",
          "3220130778636571709490905", "3588873017660047694725749", "9288991387848870159567061", "4840101673383478700737237",
          "8430916536880190158229898", "8986106490042260460547150", "2591460395957631878779378", "1816190871689680423501920",
          "0704047294563387014281341", "8544774664056811258209321", "9609294756392563447060526", "0170173859593369054590795",
          "6088985673796975810221577", "7738800757919472437622349", "5474120045253009653348388", "3930491401877849249410013",
          "1486477041403746396925337", "2955579022827592919878713", "2625547961868100985291514", "3673299809851325174555652",
          "4533398973801647859680907"]
    p2 = ["5250", "1457", "8636", "7660", "7848"]
    assert grid_search(g2, p2) == "YES"

    g3 = ["111111111111111", "111111111111111", "111111011111111", "111111111111111", "111111111111111"]
    p3 = ["11111", "11111", "11110"]
    assert grid_search(g3, p3) == "YES"
