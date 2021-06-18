# 재귀함수는 depth 제한이 있으므로 DP 알고리즘 적용
# f(n) = f(n-1) + f(n-2), f(0) = f(1) = 1

# def solution(n):
#     dp = [0] * (n) # 피보나치 수를 저장할 DP 테이블
#     dp[0] = dp[1] = 1 # 첫 번째와 2번 째 값 저장
#     for i in range(2, n):
#         dp[i] = dp[i-1] + dp[i-2] # 3번째값부터 점화식 적용
        
#     return dp[n-1] % 1234567

def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b # 파이썬의 특성을 이용하여 피보나치 수 구하기

    return a % 1234567
