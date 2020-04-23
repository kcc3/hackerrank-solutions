def hurdle_race(k, height):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem

    Hurdle race calculates how many doses the person must jump after their natural jump height k, given the hurdles.

    In short, we take the highest hurdle and subtract the jump k, and if it's negative, we return 0 as it means the
    runner can already clear the highest hurdle.  Otherwise, we know the difference is the number of doses needed to
    clear the highest hurdle.

    Args:
        k (int): the natural jump height of the runner
        height (list): list of integer hurdle heights the runner must clear

    Returns:
        int: number of doses needed to clear highest hurdle
    """
    return max(max(height) - k, 0)


if __name__ == '__main__':
    n = 100
    k = 53
    input = "86 4 83 20 6 81 58 59 53 2 54 62 25 35 79 64 27 49 32 95 100 20 58 39 92 30 67 89 58 81 100 66 73 29 75 " \
            "81 70 55 18 28 7 35 98 52 30 11 69 48 84 54 13 14 15 86 34 82 92 26 8 53 62 57 50 31 61 85 88 5 80 64 90 " \
            "52 47 43 40 93 69 70 16 43 7 25 99 12 63 99 71 76 55 17 90 43 27 20 42 84 39 96 75 1 "
    heights = list(map(int, input.rstrip().split()))
    result = hurdle_race(k, heights)
    print result
