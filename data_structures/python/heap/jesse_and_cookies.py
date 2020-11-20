import heapq


#
# Complete the cookies function below.
#
def cookies(k, A):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/jesse-and-cookies/forum

    Jesse loves cookies. He wants the sweetness of all his cookies to be greater than value K. To do this, Jesse
    repeatedly mixes two cookies with the least sweetness. He creates a special combined cookie with:

    sweetness = (1 x Least sweet cookie + 2 x 2nd least sweet cookie).

    He repeats this procedure until all the cookies in his collection have a sweetness >= K.

    You are given Jesse's cookies. Print the number of operations required to give the cookies a sweetness >= K.
    Print -1 if this isn't possible.

    Args:
        k (int): The sweetness factor to compare
        A (list): List of cookies where Ai is the sweetness of ith cookie

    Returns:
        (int): The number of operations to have all cookies equal or above k, or -1 if not possible
    """
    heapq.heapify(A)
    sweetness_operations = 0
    while len(A) >= 2:
        if A[0] >= k:
            return sweetness_operations
        sweetness = heapq.heappop(A) + (2 * heapq.heappop(A))
        heapq.heappush(A, sweetness)
        sweetness_operations += 1
    if A[0] >= k:
        return sweetness_operations
    return -1


if __name__ == "__main__":
    assert cookies(7, [1, 2, 3, 9, 10, 12]) == 2
    a = []
    for i in range(100000):
        a.append(1)
    assert cookies(105823341, a) == 99999
