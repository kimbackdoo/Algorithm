def birthdayCakeCandles(candles):
    cnt = 0
    tmp = max(candles)

    for i in range(len(candles)):
        if tmp == candles[i]: cnt += 1

    return cnt