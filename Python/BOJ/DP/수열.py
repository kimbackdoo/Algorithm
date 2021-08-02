# 증가수열인 경우와 감소수열인 경우를 나누어 각각 계산한 후 최대값을 출력

# import sys
# input = sys.stdin.readline

# n = int(input())
# numbers = list(map(int, input().split()))

# dp1 = []
# cnt = 1
# for i in range(1, n):
#   if numbers[i-1] <= numbers[i]: # 증가수열이면 cnt값을 증가시킴
#     cnt += 1
#   else: # 증가수열이 아니라면
#     dp1.append(cnt) # dp1에 cnt값 append 후 cnt 값 초기화
#     cnt = 1

# dp1.append(cnt) # numbers가 계속 증가수열이면 마지막 cnt 값은 dp1에 추가되지 않으므로 cnt값 append

# dp2 = []
# cnt = 1
# for i in range(1, n):
#   if numbers[i-1] >= numbers[i]: # 감소수열이면 cnt값을 증가시킴
#     cnt += 1
#   else: # 감소수열이 아니라면
#     dp2.append(cnt) # dp2에 cnt값 append 후 cnt 값 초기화
#     cnt = 1

# dp2.append(cnt) # numbers가 계속 감소수열이면 마지막 cnt 값은 dp2에 추가되지 않으므로 cnt값 append

# print(max(dp1 + dp2))

# 증가수열의 길이를 저장할 dp1, 감소수열의 길이를 저장할 dp2를 각각 선언하여
# 증가수열, 감소수열일 때 각각 dp1, dp2에서 그 전 값을 +1 증가시킴
# 즉, 점화식은 f(n) = f(n-1) + 1이 됨

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp1 = [1] * n # 수열의 길이는 무조건 1이상이므로 1로 초기화
dp2 = [1] * n # 수열의 길이는 무조건 1이상이므로 1로 초기화
for i in range(1, n):
  if numbers[i-1] <= numbers[i]: # 증가수열일 경우에는
    dp1[i] = dp1[i-1] + 1 # dp1 리스트에 위 점화식 적용
  if numbers[i-1] >= numbers[i]: # 감소수열일 경우에는
    dp2[i] = dp2[i-1] + 1 # dp2 리스트에 위 점화식 적용

print(max(dp1 + dp2)) # dp1, dp2에서 최대값 출력
