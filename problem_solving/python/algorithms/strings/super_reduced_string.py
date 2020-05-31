def super_reduced_string(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/reduced-string/problem

    Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest
    length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that
    match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

    Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the
    final string is empty, print Empty String

    Args:
        s (str): String to reduce

    Returns:
        str: the reduced string, or "Empty String" if it's empty
    """
    cur_string = s
    while True:
        found = False
        for i in range(1, len(cur_string)):
            if cur_string[i-1] == cur_string[i]:
                found = True
                cur_string = cur_string.replace(cur_string[i]*2, "", 1)
                break
        if not found:
            break
    if not cur_string:
        cur_string = "Empty String"
    return cur_string


if __name__ == "__main__":
    assert super_reduced_string("aaabccddd") == "abd"
    assert super_reduced_string("baab") == "Empty String"
