# 입력받은 지도에서 섬의 개수를 세면됨, bfs 알고리즘 적용
# 상하좌우, 사방 대각선 전부 탐색해야함

import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y): # bfs 정의
  move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1), (1, 1), (-1, 1)] # 상하좌우, 사방 대각선 정의
  queue = deque()
  queue.append((x, y))
  maps[x][y] = 0 # 초기 좌표값 방문 처리
  while queue:
    x, y = queue.popleft()
    for i in range(8): # 모든 경우 탐색
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < h and 0 <= ny < w and maps[nx][ny]: # 다음 좌표가 범위 안에 있고, 아직 방문하지 않았으면
        maps[nx][ny] = 0 # 방문 처리
        queue.append((nx, ny))

while True:
  w, h = map(int, input().split())
  if not w and not h: break

  maps = [list(map(int, input().split())) for _ in range(h)]
  
  answer = 0
  for i in range(h): # maps의 모든 요소를 확인하면서 방문하지 않았으면 bfs 탐색하고 count
    for j in range(w):
      if maps[i][j]:
        bfs(i, j)
        answer += 1
  
  print(answer)
