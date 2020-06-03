def happy_ladybugs(b):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/happy-ladybugs/problem

    Happy Ladybugs is a board game having the following properties:

    * The board is represented by a string, b, of length n. The i'th character of the string, b[i], denotes the i'th cell
    of the board.
        * If b[i] is an underscore (i.e., _), it means the i'th cell of the board is empty.
        * If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the i'th cell contains a ladybug of
          color b[i].
        * String b will not contain any other characters.
    * A ladybug is happy only when its left or right adjacent cell (i.e., b[i+-1]) is occupied by another ladybug having
      the same color.
    * In a single move, you can move a ladybug from its current position to any empty cell.

    Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs
    happy. For each game, print YES on a new line if all the ladybugs can be made happy through some number of moves.
    Otherwise, print NO.

    Args:
        b (str): string representing the initial positions and colors of the ladybugs

    Returns:
        str: YES or NO depending on whether we can make the ladybugs happy
    """
    letters = {}
    for i in b:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1
    # Check to see if ladybugs are happy
    underscore = False
    for l in letters:
        if l == "_":
            underscore = True
        elif letters[l] < 2:
            return "NO"
    if underscore:
        return "YES"
    # Check cases where string doesn't include "_"
    for i in range(1, len(b)-1):
        if not (b[i] == b[i+1] or b[i] == b[i-1]):
            return "NO"
    return "YES"


if __name__ == "__main__":
    # print(happy_ladybugs("B_RRBR"))
    print(happy_ladybugs("_"))
    print(happy_ladybugs("RBRB"))
    print(happy_ladybugs("RRRR"))