def sum_xor(n):
    # Find the max value it could be:
    m = 1
    while m < n:
        m *= 2
    # Iterate through and see which values satisfy sum and xor being equal
    sum_xor_equal = 0
    for i in range(m):
        if n + i == n ^ i:
            sum_xor_equal += 1
    return sum_xor_equal


if __name__ == "__main__":
    assert sum_xor(5) == 2
    assert sum_xor(10) == 4
    assert sum_xor(0) == 1
