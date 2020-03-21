def get_money_spent(keyboards, drives, b):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/electronics-shop/problem

    Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of
    each. Monica wants to spend as much as possible for the 2 items, given her budget.

    Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of
    money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead.
    She will buy only the two required items.

    Solve: Iterate through the keyboards and drives to see the maximum amount we can spend without going over total budget

    Args:
        keyboards (list): list of keyboard costs
        drives (list): list of drive costs
        b (int): budget

    Returns:
        int: the highest amount that can be spent, or -1 if not possible
    """
    cost = -1
    for keyboard in keyboards:
        for drive in drives:
            if cost < keyboard + drive <= b:
                cost = keyboard + drive
    return cost


if __name__ == "__main__":
    keyboards = [3, 1]
    drives = [5, 2, 8]
    budget = 10
    print get_money_spent(keyboards, drives, budget)