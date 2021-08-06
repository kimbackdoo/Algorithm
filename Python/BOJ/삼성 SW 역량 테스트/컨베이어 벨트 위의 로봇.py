# 문제에서 요구한대로 구현
# 컨베이너 벨트가 회전하기 때문에 큐를 생각

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
a_list = list(map(int, input().split()))

# 로봇이 담겨있는 칸을 기억해야 하므로 [벨트 번호, 로봇] 리스트로 큐를 생성, 로봇이 있는 칸은 1, 없는 칸은 0
# 처음에는 로봇이 없으므로 전부 0
belt = deque([a, 0] for a in a_list)
result, cnt = 0, 0
while cnt < k: # 4
  result += 1 # 단계 count
  
  # 1
  belt.appendleft(belt.pop()) # 벨트 회전, 즉, 제일 뒤 번호가 제일 처음 번호가 됨
  belt[n-1][1] = 0 # n번칸에서 로봇을 내리므로 n-1번째 요소의 1번째 요소를 0으로 저장함으로써 로봇 내리는 것을 표현
  
  # 2
  # 1번칸이 올리는 위치, n번칸이 내리는 위치
  # 가장 먼저 벨트에 올라간 로봇부터 이동시켜야 하므로 n-1번째 요소는 내리는 위치이므로 n-2번째 요소부터 내림차순
  for i in range(n-2, -1, -1):
    # 2-1
    if belt[i][1] and not belt[i+1][1] and belt[i+1][0] >= 1: # i번째 요소에 로봇이 있고, i+1번째 요소에 로봇이 없고, i+1번째 요소의 내구도가 1이상인 경우 
        belt[i][1] = 0 # 로봇 이동, 현재 칸 로봇 값 0
        belt[i+1][1] = 1 # 로봇 이동, 다음 칸 로봇 값 1
        belt[i+1][0] -= 1 # 로봇을 올리거나 이동할 경우 내구도가 1 감소하므로
        if not belt[i+1][0]: # i+1번째 요소의 내구도가 0인 경우 count
          cnt += 1
  belt[n-1][1] = 0 # n번 칸 로봇 내림
  
  # 3
  if belt[0][0] > 0: # 첫번째 요소의 내구도가 0보다 크면
    belt[0][1] = 1 # 로봇 올림
    belt[0][0] -= 1 # 첫번째 요소의 내구도 1 감소
    if not belt[0][0]: # 첫번째 요소의 내구도가 0인 경우 count
      cnt += 1

print(result)
