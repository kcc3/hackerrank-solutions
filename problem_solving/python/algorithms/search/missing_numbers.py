def missing_numbers(arr, brr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/missing-numbers/problem

    Numeros the Artist had two lists that were permutations of one another. He was very proud. Unfortunately, while
    transporting them from one exhibition to another, some numbers were lost out of the first list. Can you find the
    missing numbers?

    As an example, the array with some numbers missing, arr = [7, 2, 5, 3, 5, 3]. The original array of numbers
    brr = [7, 2, 5, 4, 6, 3, 5, 3]. The numbers missing are [4, 6].

    Args:
        arr (list): the array with missing numbers
        brr (list): the original array of numbers

    Returns:
        list: list of missing numbers in ascending order
    """
    for i in arr:
        brr.remove(i)
    return sorted(set(brr))


if __name__ == "__main__":
    a = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    b = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
    print(missing_numbers(a, b))