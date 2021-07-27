# 피보나치 수 점화식은 f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

n = int(input())

if n == 0: # n이 0이라면 0출력
  print(0)
else: # n이 1이상이면
  dp = [0] * (n+1)
  dp[1] = 1 # f(1) = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] # 위 점화식 적용

  print(dp[n])
