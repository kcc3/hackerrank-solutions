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
    output = []
    # Figure out the rows and columns based on string length
    rows = math.floor(math.sqrt(len(string)))
    columns = math.ceil(math.sqrt(len(string)))
    if rows * columns < len(string):
        rows += 1
    # Iterate through and populate into the rows and columns matrix
    for i in range(rows):
        chars = []
        for j in range(columns):
            if j + i * columns < len(string):
                chars.append(string[j + i * columns])
            else:
                chars.append("")
        output.append(chars)
    # Now print out the string based on columns
    result = []
    for i in range(columns):
        line = ""
        for j in range(rows):
            line += output[j][i]
        result.append(line)
    return " ".join(result)


if __name__ == "__main__":
    print(encryption("have a nice day"))
    print(encryption("feedthedog"))
    print(encryption("chillout"))