# 팩토리얼 계산을 재귀가 아닌 dp 알고리즘으로 구현
# 0! = 1! = 1
# 이항 계수 -> C(n, k) = n! // ((n-k)! * k!)

def C(n, k):
  dp = [0] * (n+1) # dp 테이블 생성
  dp[0] = dp[1] = 1 # 0! = 1! = 1
  for i in range(2, n+1):
    dp[i] = i * dp[i-1] # n! = n * (n-1)!, dp[n] = n * dp[n-1]
  
  return dp[n] // (dp[n-k] * dp[k]) # 점화식 반환

n, k = map(int, input().split())
print(C(n, k))
