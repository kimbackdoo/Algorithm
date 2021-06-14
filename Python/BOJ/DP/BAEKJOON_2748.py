# f(0) = 0, f(1) = 1
# f(n) = f(n-1) + f(n-2)

n = int(input())

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2] # 점화식 실행

print(dp[n])
