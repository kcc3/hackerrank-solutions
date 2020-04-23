def cat_and_mouse(x, y, z):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

    Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to
    determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed.
    If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

    Determine which cat catches the mouse of if the mouse escapes.

    If the distance between the mouse and the cats is the same, it escapes.
    Otherwise, the cat that is closer to the mouse will catch it first.

    Args:
        x (int): Cat A's position
        y (int): Cat B's position
        z (int): Mouse C's position

    Returns:
        string: The cat that catches the mouse or the mouse if it escapes
    """
    if abs(z - x) == abs(z - y):
        return "Mouse C"
    elif abs(z - x) > abs(z - y):
        return "Cat B"
    else:
        return "Cat A"


if __name__ == "__main__":
    print cat_and_mouse(1, 2, 3)
    print cat_and_mouse(1, 3, 2)