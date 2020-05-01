def funny_string(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/funny-string/problem

    In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny,
    create a copy of the string in reverse e.g. abc -> cba. Iterating through each string, compare the absolute
    difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of
    absolute differences is the same for both strings, they are funny.

    Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

    Args:
        s (str): String to check

    Returns:
        str: Returns "Funny" or "Not Funny" based on the results of the string
    """
    for i in range(len(s)//2):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(s[len(s)-i-1]) - ord(s[len(s)-i-2])):
            return "Not Funny"
    return "Funny"


if __name__ == "__main__":
    assert funny_string("acxz") == "Funny"
    assert funny_string("bcxz") == "Not Funny"