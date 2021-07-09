# 재귀를 사용하지 않고, dp 알고리즘(보턴업) 이용

n = int(input())

dp = [0] * (n+1) # dp 테이블 생성
dp[1] = 1 # 피보나치 수에서 0번째는 0, 1번째는 1
for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2] # 점화식 적용

print(dp[n])
