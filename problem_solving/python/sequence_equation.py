def permutation_equation(p):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/permutation-equation/problem

    Given a sequence of n integers, p(1), p(2), ..., p(n) where each element is distinct and satisfies 1 <= p(x) <= n.
    For each x where 1 <= x <= n, find any integer y such that p(p(y)) ~ x and return that value

    Args:
        p (list): list of integers p[i] where 1 <= i <= n

    Returns:
        list: list of the values that satisfy p(p(y)) ~ x
    """
    permutation = []
    for i in xrange(1, len(p)+1):
        permutation.append(p.index(p.index(i) + 1) + 1)
    return permutation


if __name__ == "__main__":
    print permutation_equation([2, 3, 1])
    print permutation_equation([4, 3, 5, 1, 2])