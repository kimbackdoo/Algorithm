# 건전지 사용량의 최솟값을 구하는 것이고, 순간이동 할 경우 건전지 사용량이 들지 않기 때문에 최대한 순간이동을 많이 해야한다. 즉, 그리디 알고리즘

# def solution(n):
#     answer = 0
#     while n != 0: # n이 0이 될때까지 반복
#         if n % 2 == 0: # 순간이동을 할 수 있으면 순간이동
#             n //= 2
#         else: # 그렇지 않으면 점프하고 건전지 사용량 count
#             n -= 1
#             answer += 1
            
#     return answer
  
def solution(n):
    return bin(n).count('1') # n을 이진수로 변환 후 1의 개수
