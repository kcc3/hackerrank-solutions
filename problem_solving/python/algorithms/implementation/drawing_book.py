def page_count(n, p):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/drawing-book/problem

    Brie's Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from
    the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book,
    page 1 is always on the right side:

    [ X | 1 ]

    When she flips page 1, she sees pages 2 and 3. Each page except the last page will always be printed on both sides.
    The last page may only be printed on the front, given the length of the book. If the book is n pages long, and she
    wants to turn to page p, what is the minimum number of pages she will turn? She can start at the beginning or the
    end of the book.

    Given n and p, find and print the minimum number of pages Brie must turn in order to arrive at page p.

    Solve: Return the minimum value of turning pages starting from the front of the book or starting from the back

    Args:
        n (int): total number of pages in the book
        p (int): the selected page we want to turn to

    Returns:
        int: minimum number of page turns needed to get to selected page
    """
    return min(p/2, n/2-p/2)


if __name__ == "__main__":
    print page_count(6, 2)
    print page_count(5, 4)