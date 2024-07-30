def plusMinus(arr):
    cnt = [0, 0, 0]

    for i in range(len(arr)):
        if arr[i] > 0: cnt[0] += 1
        elif arr[i] < 0: cnt[1] += 1
        else: cnt[2] += 1

    for i in range(len(cnt)):
        print(round(cnt[i]/len(arr), 6))