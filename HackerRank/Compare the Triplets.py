def compareTriplets(a, b):
    cnt = []
    cnt_a = 0
    cnt_b = 0

    for i in range(len(a)):
        if a[i] > b[i] : cnt_a += 1
        elif a[i] < b[i] : cnt_b += 1

    cnt.append(cnt_a)
    cnt.append(cnt_b)

    return cnt