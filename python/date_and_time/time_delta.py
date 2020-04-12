import datetime


def time_delta(t1, t2):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/python-time-delta/problem

    Function that calculates the absolute difference between two passed in times.

    Time is passed in as a string with this format: Day dd Mon yyyy hh:mm:ss +xxxx

    Args:
        t1 (str): date and time #1
        t2 (str): date and time #2

    Returns:
        str: the absolute difference between the times in total seconds
    """
    t1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs(t1-t2).total_seconds()))


if __name__ == '__main__':
    test_time1_t1 = "Sun 10 May 2015 13:54:36 -0700"
    test_time1_t2 = "Sun 10 May 2015 13:54:36 -0000"
    test_time2_t1 = "Sat 02 May 2015 19:54:36 +0530"
    test_time2_t2 = "Fri 01 May 2015 13:54:36 -0000"
    print(time_delta(test_time1_t1, test_time1_t2))
    print(time_delta(test_time2_t1, test_time2_t2))