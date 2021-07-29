# 문제를 읽어보면 정삼각형의 한 변의 길이가 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, ... 식으로 변하는 것을 알 수 있다.
# 즉, 점화식을 세워 보면 f(n) = f(n-1) + f(n-5) (n >= 6)가 됨을 알 수 있다.

# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#   n = int(input())

#   if n == 1 or n == 2 or n == 3: # n이 1, 2, 3일 경우 1 출력
#     print(1)
#   elif n == 4 or n == 5: # n이 4, 5일 경우 2 출력
#     print(2)
#   else: # n이 6 이상이면
#     dp = [0] * n # 점화식을 저장할 dp 테이블
#     dp[0] = dp[1] = dp[2] = 1 # 0, 1, 2번째 요소는 1
#     dp[3] = dp[4] = 2 # 3, 4번째 요소는 2
#     for i in range(5, n): # 5번째부터 점화식 적용
#       dp[i] = dp[i-1] + dp[i-5]
    
#     print(dp[n-1])

# n이 1부터 100까지 이므로 dp 테이블에 100까지 정삼각형의 변의 길이를 미리 저장해두고 입력 받은 값 출력

import sys
input = sys.stdin.readline

dp = [0] * 100 # 100까지 정삼각형의 변의 길이를 저장할 dp 테이블
dp[0] = dp[1] = dp[2] = 1 # 0, 1, 2번째 요소는 1
dp[3] = dp[4] = 2 # 3, 4번째 요소는 2
for i in range(5, 100): # 5번째부터 100번째까지 점화식 적용
  dp[i] = dp[i-1] + dp[i-5]

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n-1]) # 입력 받은 값에 해당하는 정삼각형의 변의 길이를 출력
