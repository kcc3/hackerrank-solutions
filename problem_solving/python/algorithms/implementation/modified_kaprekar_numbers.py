def kaprekar_numbers(p, q):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/kaprekar-numbers/problem

    A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the
    number into two integers and sum those integers, you have the same value you started with.

    Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2 * d digits long
    or (2 * d) - 1 digits long. Split the string representation of the square into two parts, l and r. The right hand
    part, r must be d digits long. The left is the remaining substring. Convert those two substrings back to integers,
    add them and see if you get n.

    Given two positive integers p and q where p is lower than q, write a program to print the modified Kaprekar numbers
    in the range between p and q, inclusive.

    Args:
        p (int): Lower integer limit
        q (int): Upper integer limit

    Returns:
        None: Outputs the numbers that satifies the requirement
    """
    kaprekar = ""
    if p == 1:
        kaprekar = "1 "
    for i in range(p, q+1):
        ii = str(i*i)
        if len(ii) > 1:
            num1 = int(ii[:-len(str(i))])
            num2 = int(ii[-len(str(i)):])
            if num1 + num2 == i and num1 and num2:
                kaprekar += "{0} ".format(i)
    if kaprekar:
        print(kaprekar)
    else:
        print("INVALID RANGE")


if __name__ == "__main__":
    kaprekar_numbers(1, 100)
    # kaprekar_numbers(297, 297)
    # kaprekar_numbers(1, 99999)
    # kaprekar_numbers(1000, 10000)