def marcs_cakewalk(calorie):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

    Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance
    to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk
    at least 2**j x c miles to maintain his weight.

    Solve:
        To calculate the minimum miles, you solve based on the highest calorie to lowest calorie cupcake

    Args:
        calorie (list): List of integers denoting the calories for each cupcake

    Returns:
        int: The minimum number of miels Marc must walk to maintain his weight
    """
    calories = 0
    for i, c in enumerate(sorted(calorie, reverse=True)):
        calories += (2 ** i * c)
    return calories


if __name__ == "__main__":
    assert marcs_cakewalk([5, 10, 7]) == 44
    assert marcs_cakewalk([1, 3, 2]) == 11
    assert marcs_cakewalk([7, 4, 9, 6]) == 79
