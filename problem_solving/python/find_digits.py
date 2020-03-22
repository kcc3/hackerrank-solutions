def find_digits(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/find-digits/problem

    An integer d is a divisor of an integer n if the remainder of n / d = 0.

    Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of
    divisors occurring within the integer.

    Args:
        n (int): integer to check

    Returns:
        int: the number of digits that divide evenly into the integer
    """
    digits = 0
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            digits += 1
    return digits


if __name__ == "__main__":
    print find_digits(12)
    print find_digits(1012)