def chocolate_feast(n, c, m):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/chocolate-feast/problem

    Function that calculates how many chocolates Bobby can purchase and eat.  Problem stated below:

    Little Bobby loves chocolate. He frequently goes to his favorite 5&10 store, Penny Auntie, to buy them. They are
    having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

    For example, Bobby has n = 15 to spend on bars of chocolate that cost c = 3 each. He can turn in m = 2 wrappers to
    receive another bar. Initially, he buys 5 bars and has 5 wrappers after eating them. He turns in 4 of them, leaving
    him with 1, for 2 more bars. After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper and
    his new bar. Once he eats that one, he has 2 wrappers and turns them in for another bar. After eating that one, he
    only has 1 wrapper, and his feast ends. Overall, he has eaten 5 + 2 + 1 + 1 = 9 bars.

    Args:
        n (int): Int representing Bobby's initial amount of money
        c (int): Int representing the cost of a chocolate bar
        m (int): Int representing the number of wrappers he can turn in for a free bar

    Returns:
        int: The number of chocolate bars Bobby can purchase and eat
    """
    # We look for the candies + wrappers
    candies = n // c
    wrappers = n // c
    while wrappers >= m:
        wrappers -= m
        wrappers += 1
        candies += 1
    return candies


if __name__ == "__main__":
    print(chocolate_feast(10, 2, 5))
    print(chocolate_feast(12, 4, 4))
    print(chocolate_feast(6, 2, 2))