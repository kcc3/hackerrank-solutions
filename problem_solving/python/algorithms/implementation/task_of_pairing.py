def task_of_pairing(freq):
    """Hackerrank Test - function that determines the maximum number of pairs of dumbells a company can sell given that
    you can sell dumbells with no greater than a 1 unit difference.

    Args:
        freq (list): Array of frequencies of dumbells, having weight i + 1

    Returns:
        int: The maximum number of pairs of dumbells the company can sell
    """
    total = 0
    for i in range(len(freq) - 1):
        total += freq[i] // 2
        if freq[i] % 2 and freq[i + 1] > 0:
            total += 1
            freq[i + 1] -= 1
    total += freq[-1] // 2
    return total


if __name__ == "__main__":
    print(task_of_pairing([3, 5, 4, 3]))