def taum_bday(b, w, bc, wc, z):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/taum-and-bday/problem

    Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants
    from Taum: one is black and the other is white. To make her happy, Taum has to buy b black gifts and w white gifts.

    - The cost of each black gift is bc units.
    - The cost of every white gift is wc units.
    - The cost of converting each black gift into white gift or vice versa is z units.

    Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

    For example, if Taum wants to buy b = 3 black gifts and w = 5 white gifts at a cost of bc = 3, wc = 4 and conversion
    cost z = 1, we see that he can buy a black gift for 3 and convert it to a white gift for 1, making the total cost of
     each white gift 4. That matches the cost of a white gift, so he can do that or just buy black gifts and white gifts.
     Either way, the overall cost is 3 * 3 + 5 * 4 = 29.

    Args:
        b (int): The number of black presents to purchase
        w: (int): The number of white presents to purchase
        bc (int): The cost of each black present
        wc (int): The cost of each white present
        z (int): The cost to switch between the present types

    Returns:
        int: the optimized cost to buy the specified presents
    """
    return b * min(bc, wc + z) + w * min(wc, bc + z)


if __name__ == "__main__":
    print taum_bday(3, 5, 3, 4, 1)
    print taum_bday(10, 10, 1, 1 , 1)
    print taum_bday(5, 9, 2, 3, 4)