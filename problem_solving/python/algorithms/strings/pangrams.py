def pangrams(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/pangrams/problem

    Roy wanted to increase his typing speed for programming contests. His friend suggested that he type the sentence
    "The quick brown fox jumps over the lazy dog" repeatedly. This sentence is known as a pangram because it contains
    every letter of the alphabet.

    After typing the sentence several times, Roy became bored with it so he started to look for other pangrams.

    Given a sentence, determine whether it is a pangram. Ignore case.

    Args:
        s (str): String to check to see if it's a pangram or not

    Returns:
        str: Return "pangram" or "not pangram" based on the results of the string
    """
    letters = {}
    for i in s.lower():
        if i not in letters.keys() and i != " ":
            letters[i] = 1
    if len(letters.keys()) == 26:
        return "pangram"
    return "not pangram"


if __name__ == "__main__":
    assert pangrams("We promptly judged antique ivory buckles for the next prize") == "pangram"
    assert pangrams("We promptly judged antique ivory buckles for the prize") == "not pangram"