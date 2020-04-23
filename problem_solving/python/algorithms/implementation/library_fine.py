def library_fine(d1, m1, y1, d2, m2, y2):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/library-fine/problem

    Your local library needs your help! Given the expected and actual return dates for a library book, create a program
    that calculates the fine (if any). The fee structure is as follows:

    1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).

    2. If the book is returned after the expected return day but still within the same calendar month and year as the
    expected return date, fine = 15 Hackos x (the number of days late).

    3. If the book is returned after the expected return month but still within the same calendar year as the expected
    return date, the fine = 500 Hackos x (the number of months late).

    4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000 Hackos.

    Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017
    or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10,000 Hackos.

    Args:
        d1 (int): return day
        m1 (int): return month
        y1 (int): return year
        d2 (int): due day
        m2 (int): due month
        y2 (int): due year

    Returns:
        int: the amount of hackos owed based on the book date returned and date due
    """
    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2 and d1 > d2:
            return 15 * (d1 - d2)
    return 0


if __name__ == "__main__":
    print library_fine(6, 9, 2020, 4, 9, 2020)
    print library_fine(6, 9, 2020, 4, 8, 2020)