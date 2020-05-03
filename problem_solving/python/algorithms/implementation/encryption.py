import math


def encryption(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/encryption/problem

    Encryption function based on the specifics as provided in the challenge.

    Args:
        s (str): The string to encrypt

    Returns:
        str: The string after passing through specified encryption
    """
    string = s.replace(" ", "")
    columns = math.ceil(math.sqrt(len(string)))
    line = ""
    for i in range(columns):
        line += string[i::columns] + " "
    return line


if __name__ == "__main__":
    print(encryption("have a nice day"))
    print(encryption("feedthedog"))
    print(encryption("chillout"))