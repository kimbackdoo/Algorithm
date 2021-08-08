# 문제에서 주어진 조건을 그대로 구현하면 되는 시뮬레이션 문제
# 처음에 조건대로 구현하지 않아서 틀림..
# 차례대로 조건을 구현하는 것이 중요

import sys
input = sys.stdin.readline

from collections import defaultdict

def condition1(nums): # 조건 1, 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
  dic = defaultdict(list) # 칸의 개수에 따른 좌표값을 저장하기 위해 defaultdict(list)사용, 이때 list인 이유는 칸의 개수가 동일할 수 있으므로 여러 개의 좌표값이 나올 수 있음
  for x in range(n):
    for y in range(n):
      if not classroom[x][y]: # 비어있는 칸 중에서
        cnt = 0
        for k in range(4):
          nx, ny = x + move[k][0], y + move[k][1]
          # 인접한 칸은 상하좌우 연결된 칸을 의미
          if 0 <= nx < n and 0 <= ny < n and classroom[nx][ny] in nums:  # 좋아하는 학생이 인접한 칸 개수 count
            cnt += 1
          
        dic[cnt].append((x, y)) # 개수에 따라 좌표값 append, 예를 들어, 1: [(0, 1), (1, 1)] 이런식으로 저장됨

  return dic[max(dic)] # 칸의 개수가 가장 많은 칸의 좌표값들을 return

def condition2(next): # 조건 2, 조건 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
  dic = defaultdict(list)
  for x, y in next: # 조건 1을 만족하는 칸들 중에서
    cnt = 0
    for k in range(4):
      nx, ny = x + move[k][0], y + move[k][1]
      if 0 <= nx < n and 0 <= ny < n and not classroom[nx][ny]: # 인접한 칸 개수 count
        cnt += 1
      
    dic[cnt].append((x, y)) # 개수에 따라 좌표값 append
  
  return dic[max(dic)] # 칸의 개수가 가장 많은 칸의 좌표값들을 return

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n**2)]

classroom = [[0] * n for _ in range(n)] # 자리배치할 리스트
move = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상하좌우 확인해야 하기 때문
student = {} # 학생 번호에 따라 좌표값 저장 예를 들어, 3: (2, 1) 이런식으로 저장
for i in range(n**2):
  next = condition1(nums[i][1:]) # 조건 1, next의 크기가 1개이든, 여러개이든 제일 처음값이 classroom 리스트에 저장되므로 한번에 조건 1, 2, 3을 진행
  next = condition2(next) # 조건 2
  next.sort() # 조건 3
  student[nums[i][0]] = next[0] # student에 학생번호에 따라 해당 좌표값 저장
  classroom[next[0][0]][next[0][1]] = nums[i][0] # classroom에 학생 배치

score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000} # 개수에 따른 만족도 점수
result = 0
for i in range(n**2):
  x, y = student[nums[i][0]] # 학생 번호에 해당하는 좌표값을 불러옴
  cnt = 0
  for k in range(4):
    nx, ny = x + move[k][0], y + move[k][1]
    if 0 <= nx < n and 0 <= ny < n and classroom[nx][ny] in nums[i][1:]: # 상하좌우 확인했을때 그 값이 좋아하는 학생 리스트에 속하면 count
        cnt += 1
  
  result += score[cnt] # 개수에 따라 만족도 점수 덧셈

print(result)
