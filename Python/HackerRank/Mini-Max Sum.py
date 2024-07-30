def miniMaxSum(arr):
    result = [0, 0]

    arr.sort()
    for i in range(len(arr)):
        if i==4: break
        result[0] += arr[i]
        result[1] += arr[len(arr)-1-i]

    print(str(result[0]) + ' ' + str(result[1]))