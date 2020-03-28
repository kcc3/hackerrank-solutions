def append_and_delete(s, t, k):
    """Hackerrnnk Problem: https://www.hackerrank.com/challenges/append-and-delete/problem

    You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

    1. Append a lowercase English alphabetic letter to the end of the string.
    2. Delete the last character in the string. Performing this operation on an empty string results in an empty string.

    Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly
    k of the above operations on . If it's possible, print Yes. Otherwise, print No.

    For example, strings s = [a, b, c] and t = [d, e, f]. Our number of moves, k = 6. To convert s to t, we first delete
    all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6th move, you will have
    the matching string. If there had been more moves available, they could have been eliminated by performing multiple
    deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.

    Args:
        s (str): the starting string
        t (str): the end desired string
        k (int): the number of operations to get to desired string

    Returns:
        str: Return "Yes" if we can append and delete to get to desired string, and "No" if we cannot with k actions
    """
    # First, find the length of the matching portion of the strings
    match_length = 0
    for i in xrange(0, min(len(s), len(t))):
        if s[i] == t[i]:
            match_length += 1
        else:
            break
    # Iterate through and check the various different cases
    # Case 1 - the string to match is greater than k, so not possible (ie - "abcdef", "abcdefghijkl, and k = 3)
    if (len(s) - match_length) + (len(t) - match_length) > k:
        return "No"
    # Case 2 - the string to match is smaller than or equal to k and the match steps and k are both either even or odd,
    # so it's possible (ie - "hello", "hellowor", k = 3) or ("hello", "hellowr", k = 2)
    elif ((len(s) - match_length) + (len(t) - match_length)) % 2 == k % 2:
        return "Yes"
    # Case 3 - We can replace if k is greater than the length of the strings, as we can just call "delete" until we
    # need to append
    elif len(s) + len(t) < k:
        return "Yes"
    # Case 4 - the string to match isn't possible because of even and odd mismatch
    # (ie, if we have the case of "you" and "your" and k = 2)
    return "No"


if __name__== "__main__":
    start = "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
    end = "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
    k = 100
    print append_and_delete(start, end, k)
    print append_and_delete("you", "your", 2)