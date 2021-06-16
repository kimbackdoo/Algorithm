# 바닥장식의 모든 개수를 구하기 위해 bfs 탐색
# "-"인 경우 좌우로 움직이면서 같을 경우 count 하지 않음
# "|"인 경우 상하로 움직이면서 같을 경우 count 하지 않음

from collections import deque

n, m = map(int, input().split())

deco = []
for _ in range(n):
  deco.append(list(input()))
# x, y는 좌우 또는 상하로 움직일 수 있음
dx = [-1, 1]
dy = [-1, 1]

def bfs(x, y, d): # bfs 구현
  queue = deque()
  queue.append((x, y))
  deco[x][y] = "o" # 초기 좌표 값 방문했으므로 "o"로 표시
  while queue:
    x, y = queue.popleft()
    for i in range(2): 
      if d == "|": # 매개변수로 들어온 d가 |라면
        nx = x + dx[i] # 상하로 움직임
        if 0 <= nx < n and deco[nx][y] == d: # dx가 범위에 있고 다음 이동할 곳이 |이라면 모두 탐색
          queue.append((nx, y))
          deco[nx][y] = "o" # 방문 표시
      else: # d가 -라면
        ny = y + dy[i] # 좌우로 움직임
        if 0 <= ny < m and deco[x][ny] == d: # dy가 범위에 있고 다음 이동할 곳이 -이라면 모두 탐색
          queue.append((x, ny))
          deco[x][ny] = "o" # 방문 표시

result = 0
for i in range(n):
  for j in range(m):
    if deco[i][j] == "-": # -인 경우 모두 체크하면서 count, 좌우로 이어져 있으면 count하지 않고 떨어져 있을 경우만 count
      bfs(i, j, "-")
      result += 1
    elif deco[i][j] == "|": # |인 경우 모두 체크하면서 count, 상하로 이어져 있으면 count하지 않고 떨어져 있을 경우만 count
      bfs(i, j, "|")
      result += 1

print(result)
