"""
def strange_counter(t):
    cur_start = 3
    counter = 3
    for i in range(1, t):
        counter -= 1
        if counter == 0:
            cur_start *= 2
            counter = cur_start
    return counter
"""


def strange_counter(t):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/strange-code/problem

    Bob has a strange counter. At the first second, it displays the number 3. Each second, the number displayed by the
    counter decrements by 1 until it reaches 1.

    The counter counts down in cycles. In next second, the timer resets to 2 x the initial number of the prior cycle and
    continues counting down. The diagram below shows the counter values for each time t in the first three cycles:

    time | value
    1      3
    2      2
    3      1

    time | value
    4      6
    5      5
    6      4
    7      3
    8      2
    9      1

    Find and print the value displayed by the counter at time t.

    Args:
        t: an integer to find the count for

    Returns:
        int: the value based on the strange counter
    """
    cur_start = 3
    while t > cur_start:
        t -= cur_start
        cur_start *= 2
    # Now find the value to return
    return cur_start - t + 1


if __name__ == "__main__":
    print(strange_counter(4))
    print(strange_counter(12))
