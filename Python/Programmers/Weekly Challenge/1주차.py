# 문제에 나온대로 구현

# def solution(price, money, count):
#     answer = sum([price * i for i in range(1, count + 1)]) - money # sum 함수를 이용하여 총 필요한 놀이기구 이용 금액을 구함
#     return answer if answer > 0 else 0 # answer이 0보다 크면 돈이 모자른 것이고, 0보다 작으면 돈이 남는 것이기 때문에 돈이 모자르면 answer, 돈이 남으면 0 return
  
# def solution(price, money, count):
#     answer = sum([price * i for i in range(1, count + 1)]) - money
#     return max(0, answer) # if문을 사용하지 않고 max 함수를 이용하여 return

# 총 필요한 이용금액은 price * 1 + price * 2 + price * 3 + price * 4 + ... + price * (count + 1)
# 즉, price * (1 + 2 + 3 + 4 + ... + count + 1)이므로 price * count * (count + 1) // 2 공식을 세울 수 있음

def solution(price, money, count):
    answer = price * count * (count + 1) // 2 - money # 공식 적용
    return max(0, answer) # max 함수를 이용하여 최대값 return
