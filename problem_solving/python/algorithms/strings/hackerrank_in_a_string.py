def hackerrank_in_string(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

    Args:
        s (str): String to check to see if Hackerrank is contained in it

    Returns:
        str: Return "YES" or "NO" based on whether we find hackerrank in the string or not
    """
    hackerrank = "hackerrank"
    current_char = 0
    for i in s:
        if i == hackerrank[current_char]:
            current_char += 1
            if current_char == len(hackerrank):
                return "YES"
    return "NO"


if __name__ == "__main__":
    assert hackerrank_in_string("hereiamstackerrank") == "YES"
    assert hackerrank_in_string("hackerworld") == "NO"
