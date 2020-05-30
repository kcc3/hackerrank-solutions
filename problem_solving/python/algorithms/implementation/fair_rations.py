def fair_rations(B):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/fair-rations/problem

    You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your subjects are in a line,
    and some of them already have some loaves. Times are hard and your castle's food stocks are dwindling, so you must
    distribute as few loaves as possible according to the following rules:

    1. Every time you give a loaf of bread to some person , you must also give a loaf of bread to the person immediately
    in front of or behind them in the line (i.e., persons i+1 or i-1).
    2. After all the bread is distributed, each person must have an even number of loaves.

    Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must
    distribute to satisfy the two rules above. If this is not possible, print NO.

    Args:
        B (list): an array of integers that represent the number of loaves each persons starts with

    Returns:
        int, str: the number of loaves to ration, or "NO" if it's not possible to ration
    """
    # If in the line, people are holding an odd number of loaves, it is not possible to distribute evenly
    if sum(B) % 2:
        return "NO"
    # Else, we determine the number of loaves needed to distribute to have everyone with an even number of loaves
    else:
        ration = 0
        for i in range(len(B)-1):
            if B[i] % 2:
                B[i] += 1
                B[i+1] += 1
                ration += 2
        return ration


if __name__ == "__main__":
    assert fair_rations([2, 3, 4, 5, 6]) == 4
    assert fair_rations([1, 2]) == "NO"
