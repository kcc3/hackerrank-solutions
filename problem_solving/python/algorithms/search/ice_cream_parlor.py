def ice_cream_parlor(m, arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/icecream-parlor/problem

    Sunny and Johnny like to pool their money and go to the ice cream parlor. Johnny never buys the same flavor that
    Sunny does. The only other rule they have is that they spend all of their money.

    Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

    Args:
        m (int): Total amount of pooled money
        arr (list): List of the costs of the different flavors of ice cream

    Returns:
        list: List containing the indices of the two flavors of ice cream that add up to the total pooled money
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1, j+1]


if __name__ == "__main__":
    print(ice_cream_parlor(4, [1, 4, 5, 3, 2]))