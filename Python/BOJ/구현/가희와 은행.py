# 문제에 나온대로 구현
# c초가 지났을 때를 기준으로 오름차순 정렬되어 있어야 하므로 heap을 사용하여 입력받을 때 마다 c초를 기준으로 오름차순 정렬
# 1. 대기 큐 맨 앞에 p 손님의 업무를 처리하고 처리하는 동안 은행에 도착한 손님이 있는지 확인
# 1.1 도착한 손님이 있으면 도착한 손님 모두 도착한 순서대로 대기큐에 append
# 2. 은행에 도착한 손님이 없고 p 손님의 t가 0이 아니라면 다시 p 손님의 업무를 처리하고 1번부터 반복

import sys
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque
import heapq

N, T, W = map(int, input().split())

queue = deque()
for _ in range(N):
  t, p = map(int, input().split())
  queue.append((t, p)) # 맨 앞에 대기 큐에 손님 추가

M = int(input())
wait = []
for _ in range(M):
  t, p, c = map(int, input().split())
  heapq.heappush(wait, (c, t, p)) # c초를 기준으로 heap을 생성하여 입력받을 때마다 오름차순 정렬

result = []
time = 0
while queue: # 모든 손님의 업무를 처리할 때까지 반복
  p, t = queue.popleft() # 대기 큐 맨 앞의 손님의 업무를 처리
  if t > T: # T초보다 크다면
    result.extend([p] * T) # T초만큼 업무를 처리
    time += T # T초만큼 업무시간을 더해줌
    t -= T # p 손님의 업무에 필요한 시간을 T만큼 감소
  else: # T초보다 작거나 같다면
    result.extend([p] * t) # t초만큼 업무를 처리
    time += t # t초만큼 업무시간을 더해줌
    t = 0 # p 손님의 업무가 마무리 되었으므로 t = 0

  while wait: # p 손님의 업무를 처리할 동안 은행에 도착한 손님이 있는지 확인하면서 있으면 도착한 모든 손님 대기 큐에 append
    if wait[0][0] <= time: # wait은 오름차순 정렬되어 있으므로 맨 앞의 손님이 p 손님의 업무를 처리하는 동안 도착하였다면
      c, a, b = heapq.heappop(wait) # pop
      queue.append((a, b)) # append
    else: # 아직 도착 안한 상태면 break
      break

  if t != 0: # p 손님의 업무가 다 끝나지 않았으면 즉, 0이 아니라면
    queue.append((p, t)) # 대기 큐 맨 뒤로 append

for i in range(W):
  output(f'{result[i]}\n')
