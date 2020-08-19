def flipping_bits(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/flipping-bits/problem

    You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and print the result as
    an unsigned integer.

    Solve:
        format the integer into a binary and then iterate through and flip each bit. Return the resulting flipped binary
        in integer form.

    Args:
        n (int): integer to process

    Returns:
        int: decimal value of the resulting unsigned integer
    """
    n_binary = "{0:032b}".format(n)
    flipped = "".join("1" if x == "0" else "0" for x in n_binary)
    return int(flipped, 2)


if __name__ == "__main__":
    assert flipping_bits(2147483647) == 2147483648
    assert flipping_bits(1) == 4294967294
    assert flipping_bits(0) == 4294967295
