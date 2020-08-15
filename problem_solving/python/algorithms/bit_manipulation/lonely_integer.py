def lonely_integer(a):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/lonely-integer/problem

    You will be given an array of integers. All of the integers except one occur twice. That one is unique in the array.

    Given an array of integers, find and print the unique element.

    For example, a = [1, 2, 3, 4, 3, 2, 1], the unique element is 4.

    Solve:
        Utilize XOR function for this answer.  If each int occurs twice, applying XOR twice will always result in 0,
        and XOR once will return the integer, so the one value that occurs only once will be the resulting final answer

    Args:
        a (array): array of integers where all of them occur twice except for one

    Returns:
        int: the integer that only occurs once in the array
    """
    val = 0
    for i in a:
        val = val ^ i
    return val


if __name__ == "__main__":
    assert lonely_integer([0, 0, 1, 2, 1]) == 2
    assert lonely_integer([1, 2, 3, 4, 3, 2, 1]) == 4

