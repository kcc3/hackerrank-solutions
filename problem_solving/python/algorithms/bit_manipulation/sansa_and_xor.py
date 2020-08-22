def sansa_xor(arr):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/sansa-and-xor/problem

    Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing
    the values thus obtained. Determine this value.

    Solve:
        By going through and XOR'ing the subarrays, you can determine that for even numbered arrays, you always end up
        with 0 because you XOR each value in the array with itself which always returns 0.  For example, for a subarray
        [1, 2], you would have 1 XOR 2 XOR (1 XOR 2), so 1 and 2 both show up twice and will return 0.

        For arrays of odd length, you can determine that each value of an even index position shows up an odd number of
        times, and values in an odd index position in the array show up an even number of times.  Knowing this, we can
        determine that the values in the odd index positions will once again 0 themselves out, so all that is left is for
        us to XOR each value in the array in an even index position. That value is the result and the answer.

    Args:
        arr: array of integers to test

    Returns:
        int: The result after running through sansa's XOR algorithm
    """
    if len(arr) % 2:
        val = 0
        for x in arr[::2]:
            val = val ^ x
        return val
    else:
        return 0


if __name__ == "__main__":
    assert sansa_xor([98, 74, 12]) == 110
    assert sansa_xor([50, 13, 2]) == 48
