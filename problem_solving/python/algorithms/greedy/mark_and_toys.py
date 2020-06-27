def maximum_toys(prices, k):
    """https://www.hackerrank.com/challenges/mark-and-toys/problem

    Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There
    are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to
    spend, and he wants to maximize the number of toys he buys with this money.

    Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?

    Args:
        prices (list): Array of prices of toys
        k (int): Mark's budget

    Returns:
        int: The total number of toys Mark can purchase
    """
    prices.sort()
    count = 0
    for i in prices:
        if k - i < 0:
            break
        k -= i
        count += 1
    return count


if __name__ == "__main__":
    print(maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50))
