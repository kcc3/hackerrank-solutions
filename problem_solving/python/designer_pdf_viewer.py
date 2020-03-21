def designer_pdf_viewer(h, word):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

    When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle.
    In this PDF viewer, each word is highlighted independently. For example:

    Highlighted Text:
    abc def ghi

    In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights
    given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

    Args:
        h (list): list of the heights of the 26 letters
        word (string): the string word we want to determine the highlighted area for

    Returns:
        int: the area of the highlighted word
    """
    max_height = 0
    for i in word:
        val = h[ord(i) - 97]
        if val > max_height:
            max_height = val
    return max_height * len(word)


if __name__ == "__main__":
    word_heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"
    print designer_pdf_viewer(word_heights, word)