from itertools import combinations


def alternate(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/two-characters/problem

    In this challenge, you will be given a string. You must remove characters until the string is made up of any two
    alternating characters. When you choose a character to remove, all instances of that character must be removed. Your
    goal is to create the longest string possible that contains just two alternating letters.

    As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd.
    Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at
    any point would not result in a valid string.

    Args:
        s (str): String to check for maximum alternating letters

    Returns:
        int: The integer length of the string that has the maximum length of alternating letters
    """
    letters = set(s)
    max_length = 0
    if len(letters) < 2:
        return max_length
    # Iterating through to get all of the different combinations of letters of total number of diff letters - 2.
    # We want to take each of these iterations and remove those letters from the string to create the string that
    # contains two different letters, and then check to see if that string then has alternating characters.
    for comb in combinations(letters, len(letters)-2):
        current_string = s
        # Remove those letters from the string to create a string with just two letters
        for letter in comb:
            current_string = current_string.replace(letter, "")
        # Iterate through to see if the string now has alternating letters and record the length if it's the current max
        prev = None
        count = 0
        for letter in current_string:
            if letter != prev:
                prev = letter
                count += 1
            else:
                count = 0
                break
        if count > max_length:
            max_length = count
    return max_length


if __name__ == "__main__":
    # print(alternate("beabeefeabx"))
    # print(alternate("asvkugfiugsalddlasguifgukvsa"))
    # print(alternate("a"))
    print(alternate("aaaaa"))