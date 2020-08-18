def maximizing_xor(l, r):
    xor_val = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            xor = i ^ j
            if xor > xor_val:
                xor_val = xor
    return xor_val


if __name__ == "__main__":
    print(maximizing_xor(11, 100))
