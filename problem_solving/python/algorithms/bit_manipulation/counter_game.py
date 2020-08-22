def counter_game(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/counter-game/problem

    Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2. If it
    is, they divide it by 2. If not, they reduce it by the next lower number which is a power of 2. Whoever reduces the
    number to 1 wins the game. Louise always starts.

    Given an initial value, determine who wins the game.

    Solve:
        We can efficiently solve this by doing bit checking on the value.  For the value to be a power of 2, it can have
        only one "1" in its binary form, so we convert the int to a binary string and check for the number of "1"s in
        the string.  If the count is 1, then we divide by 2.  If it's not, reducing it by the next lowest number that is
        a power of 2 is simply replacing the highest significant 1 bit to a 0, and the continuing the loop. Once we reach
        1, we count the number of turns taken to determine who won the game.

    Args:
        n (int): The initial value for the game

    Returns:
        str: The winner of the game, either "Richard" or "Louise"
    """
    winner = ["Louise", "Richard"]
    turns = 1
    while n != 1:
        bin = "{0:b}".format(n)
        val = bin.count("1")
        if val > 1:
            bin = bin.replace("1", "0", 1)
            n = int(bin, 2)
        else:
            n = int(bin, 2) // 2
        turns += 1
    return winner[turns % 2]


if __name__ == "__main__":
    assert counter_game(6) == "Richard"
    assert counter_game(132) == "Louise"
