from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  matrix[x][y] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < h and 0 <= ny < w:
        if matrix[nx][ny] == 1 or matrix[x][y] == 1:
          queue.append((nx, ny))
          matrix[nx][ny] = 0

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  matrix = []
  for _ in range(h):
    matrix.append(list(map(int, input().split())))

  move = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

  result = 0
  for i in range(h):
    for j in range(w):
      if matrix[i][j] == 1:
        bfs(i, j)
        result += 1

  print(result)
  
# dfs
# 재귀호출 오류..
def dfs(x, y):
  if 0 <= x < h and 0 <= y < w:
    if matrix[x][y] == 1:
      matrix[x][y] = 0
      for i in range(8):
        dfs(x + move[i][0], y + move[i][1])
