def decent_number(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

    Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. Sherlock's
    companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, The Beast.

    Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting The Beast
    with a virus. He also gives him a clue: an integer. Sherlock determines the key to removing the virus is to find the
    largest Decent Number having that number of digits.

    A Decent Number has the following properties:

    1. Its digits can only be 3's and/or 5's.
    2. The number of 3's it contains is divisible by 5.
    3. The number of 5's it contains is divisible by 3.
    4. It is the largest such number for its length.

    Args:
        n (int): The number of digits in the number

    Returns:
        None: Prints out the decent number or -1 if no such number exists
    """
    s = ""
    while n >= 1:
        # If the number is divisible by 3, we append a set of "555" to front of the string
        if n % 3 == 0:
            s = "{0}{1}".format("555"*(n//3), s)
            break
        # Else we subtract 5, append the string of "333" to the end of string and iterate again
        elif n >= 5:
            s = "{0}{1}".format(s, "33333")
            n -= 5
        # If it doesn't satisfy either condition, it's not possible to create a decent number
        else:
            s = "-1"
            break
    print(s)


if __name__ == "__main__":
    decent_number(1)
    decent_number(11)
