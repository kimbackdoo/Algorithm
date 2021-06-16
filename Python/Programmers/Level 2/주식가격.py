# 문제에서 요구하는 건 현재 시점의 가격이 얼마동안 안떨어지는지 체크하는 것
# 예를 들어 [1, 2, 3, 2, 3, 1]에서 첫번째 2는 마지막 1에서 가격이 떨어지는 것이므로 총 4초간 가격이 안떨어지는 것

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i, len(prices)):
#             if i != j: # i와 j가 같지 않고
#                 if prices[i] <= prices[j]: # 현재 시점보다 가격이 클 때 count
#                     cnt += 1
#                 else: # 얼마동안 안떨어지는지 체크하는 것이므로 현재시점보다 가격이 작을때도 count하고 break
#                     cnt += 1
#                     break
                
#         answer.append(cnt)
        
#     return answer
  
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]: break # 현재 시점보다 가격이 작을 때 break
            else: answer[i] += 1 # 현재 시점보다 가격이 크거나 같을 때 count

    return answer
