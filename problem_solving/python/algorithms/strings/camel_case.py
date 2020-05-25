def camel_case(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/camelcase/problem

    Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following properties:

    - It is a concatenation of one or more words consisting of English letters.
    - All letters in the first word are lowercase.
    - For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

    Given s, print the number of words in s on a new line.

    For example, s="oneTwoThree". There are 3 words in the string.

    Args:
        s (str):

    Returns:
        int: The number of words in the string
    """
    return len([i for i in s if i.isupper()]) + 1


if __name__ == "__main__":
    assert camel_case("saveChangesInTheEditor") == 5
