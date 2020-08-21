def alternating_characters(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/alternating-characters/problem

    You are given a string containing characters A and B only. Your task is to change it into a string such that there
    are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

    Your task is to find the minimum number of required deletions.

    For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.

    Args:
        s (str): the string to check

    Returns:
        int: the number of deletions needed to change s into a string with no matching adjacent characters
    """
    prev = ""
    deletes = 0
    for i in s:
        if i == prev:
            deletes += 1
        prev = i
    return deletes


if __name__ == "__main__":
    assert alternating_characters("AAAA") == 3
    assert alternating_characters("BBBBB") == 4
    assert alternating_characters("ABABABAB") == 0
    assert alternating_characters("BABABA") == 0
    assert alternating_characters("AAABBB") == 4
