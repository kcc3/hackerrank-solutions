def viral_advertising(n):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/strange-advertising/problem

    Advertising function where starting at 5, each day, floor(n/2) people like an ad and share with 3 other friends.
    At the beginning of the second day, floor(5/2) x 3 = 2 x 3 = 6 people receive the advertisement.

    Each day, floor(recipients/2) of the recipients like the ad and will share it with 3 friends on the following day.
    Assuming nobody receives the ad twice, determine how many people have liked the ad by the end of a given day, beginning
    with launch day as day 1.

    Args:
        n: day to return the cumulative people that like the ad

    Returns:
        int: number of people who like the ad given a certain day
    """
    cumulative = 0
    shared = 5
    for i in xrange(n):
        liked = shared / 2
        cumulative += liked
        shared = liked * 3
    return cumulative


if __name__ == "__main__":
    print viral_advertising(3)
    print viral_advertising(4)