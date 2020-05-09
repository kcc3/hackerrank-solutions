def bigger_is_greater(w):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem

    Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

    - It must be greater than the original word
    - It must be the smallest word that meets the first condition

    Args:
        w (str): The word to swap

    Returns:
        str: Return the next highest lexicographical word or "no answer"
    """
    # Find non-increasing suffix
    arr = [c for c in w]
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return "".join(arr)


if __name__ == "__main__":
    print(bigger_is_greater("zzzayybbaa"))
    print(bigger_is_greater("zyyxwwtrrnmlggfeb"))