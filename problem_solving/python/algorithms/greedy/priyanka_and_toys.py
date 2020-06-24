def toys(w):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/priyanka-and-toys/problem

    Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest
    cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement
    that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight
    item. All items meeting that requirement will be shipped in one container.

    Solve:
        We sort the array, and then we iterate through the list seeing if each order fits within the current lowest order's
        weight.  If it does, we can continue on, and if it doesn't, we then create a new "container" as this order no
        longer fits within the previous order limit, and continue on through the orders.

    Args:
        w (list): Array representing the weighted orders

    Returns:
        int: The minimum number of containers needed to ship the orders
    """
    containers = 1
    w.sort()
    cur_lowest = w[0]
    # Iterate through the sorted list, and add a container if the next weighted order doesn't fit within the current
    # lowest order's weight + 4
    for i in range(1, len(w)):
        if w[i] > cur_lowest + 4:
            cur_lowest = w[i]
            containers += 1
    return containers


if __name__ == "__main__":
    print(toys([1, 2, 3, 21, 7, 12, 14, 21]))
