def diagonalDifference(arr):
    arrLen = len(arr[0])
    result_r = 0
    result_l = 0

    for i in range(arrLen):
        result_r += arr[i][i]
        result_l += arr[i][arrLen-1-i]

    return abs(result_r - result_l)