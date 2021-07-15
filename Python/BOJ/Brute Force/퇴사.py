# 처음에는 해당 총 상담일 이후의 모든 경우를 생각하지 않고 한가지 경우만 생각
# 모든 경우를 생각하기 위해 dfs 탐색

import sys
input = sys.stdin.readline

n = int(input())

consult = []
for i in range(n):
  t, p = map(int, input().split())
  if (t+i) <= n: # 총 상담일이 n보다 크면 상담이 안되므로 총 상담일이 n보다 작거나 같은 경우만 append
    consult.append((i+1, t, p))

def dfs(idx): # dfs 구현
  stack = [(idx, consult[idx][2])] # (인덱스, 이익) 튜플로 모든 경우를 계산
  result = 0
  while stack:
    idx, total = stack.pop()
    result = max(result, total) # result에 해당 탐색에서 최대 이익을 저장
    for i in range(idx+1, len(consult)): # idx번째 요소 다음부터 탐색
      if (consult[idx][0] + consult[idx][1]) <= consult[i][0]: # 총 상담일이 다음 상담 시작일보다 작거나 같은 경우 전부 append
        stack.append((i, total + consult[i][2]))

  return result

result = 0
for i in range(len(consult)): # 모든 요소 dfs 탐색
  result = max(result, dfs(i))

print(result)
