def utopian_tree(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/utopian-tree/problem

    Find the current height of a tree that for each growth cycle in spring, doubles its height, and then each summer,
    adds one meter.  Tree starts at 1 meter.

    Solve: iterate through and grow based on the cycle

    Args:
        n (int): growth cycle number

    Returns:
        int: height of the tree at given growth cycle
    """
    current_height = 1
    for i in xrange(n):
        if i % 2 == 0:
            current_height *= 2
        else:
            current_height += 1
    return current_height


if __name__ == "__main__":
    print utopian_tree(0)
    print utopian_tree(1)
    print utopian_tree(4)