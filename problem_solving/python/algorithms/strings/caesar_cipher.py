import string


def caesar_cipher(s, k):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

    Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
    letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front
    of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

    ---
    Original alphabet:      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
    ---

    Args:
        s (str): string message to encrypt
        k (int): the number of letters to shift for the encryption

    Returns:
        str: converted string based on the cipher
    """
    converted_string = ""
    for i in s:
        if 65 <= ord(i) <= 90:
            converted_string += string.ascii_uppercase[(ord(i) + k - 65) % 26]
        elif 97 <= ord(i) <= 122:
            converted_string += string.ascii_lowercase[(ord(i) + k - 97) % 26]
        else:
            converted_string += i
    return converted_string


if __name__ == "__main__":
    print(caesar_cipher("middle-Outz", 2))
    print(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life"), 5)