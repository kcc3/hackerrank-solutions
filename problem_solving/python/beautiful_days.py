def beautiful_days(i, j, k):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

    Lily likes to play games with integers. She has created a new game where she determines the difference between a
    number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9.
    The number 120 reversed is 21, and their difference is 99.

    Given a range of numbered days [i ... j],  and a number k, determine the number of days in the range that are
    beautiful. Beautiful numbers are defined as numbers where abs(i - reverse(i)) is evenly divisible by k.

    Args:
        i (int): starting day value
        j (int): ending day value
        k (iut): number k to divide into to determine if it is a beautiful day

    Returns:
        (int): number of beautiful days between i and j
    """
    beautiful_days_count = 0
    for day in xrange(i, j + 1):
        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            beautiful_days_count += 1
    return beautiful_days_count


if __name__ == "__main__":
    print beautiful_days(20, 23, 6)
