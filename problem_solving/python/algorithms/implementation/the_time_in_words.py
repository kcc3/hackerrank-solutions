def time_in_words(h, m):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/the-time-in-words/problem

    Given the time in numerals we may convert it into words, as shown below:

    ----------------------------------------------
    | 5:00 | -> | five o' clock                  |
    | 5:01 | -> | one minute past five           |
    | 5:10 | -> | ten minutes past five          |
    | 5:15 | -> | quarter past five              |
    | 5:30 | -> | half past five                 |
    | 5:40 | -> | twenty minutes to six          |
    | 5:45 | -> | quarter to six                 |
    | 5:47 | -> | thirteen minutes to six        |
    | 5:28 | -> | twenty eight minutes past five |
    ----------------------------------------------

    At minutes = 0, use o' clock. For 1 <= minutes <= 30, use past, and for 30 < minutes use to. Note the space between
    the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the
    format described.

    Args:
        h (int): hour of the day
        m (int): minutes after the hour

    Returns:
        str: string representation of the time
    """
    time = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    # We check for a certain set of cases:
    # Case 1 - we're on the hour, so we use o' clock
    if m == 0:
        return "{0} o' clock".format(time[h-1])
    # Case 2 - we're one minute after, so we use minute (versus minutes later on to describe the time)
    if m == 1:
        return "{0} minute past {1}".format(time[m-1], time[h-1])
    # Case 3 - we're a quarter past the hour
    if m == 15:
        return "quarter past {0}".format(time[h-1])
    # Case 4 - we're half past the hour
    if m == 30:
        return "half past {0}".format(time[h-1])
    # Case 5 - we're a quarter to the next hour
    if m == 45:
        return "quarter to {0}".format(time[h])
    # Case 6 - we check for minutes after the hour, which is until we hit minute 30
    if m < 30:
        return "{0} minutes past {1}".format(time[m-1], time[h-1])
    # Case 7 - this covers the cases where the minutes are after 30 so we're mintues to the next hour
    return "{0} minutes to {1}".format(time[59-m], time[h])


if __name__ == "__main__":
    print time_in_words(5, 47)
    print time_in_words(3, 00)
    print time_in_words(7, 15)
    print time_in_words(7, 29)
