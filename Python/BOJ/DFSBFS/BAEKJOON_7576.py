from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
          matrix[nx][ny] = matrix[x][y] + 1
          queue.append((nx, ny))

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      queue.append((i, j))

bfs()
isZero = False
result = 0
for mat in matrix:
  if mat.count(0) >= 1:
    isZero = True
  if result < max(mat):
    result = max(mat)

if isZero: print(-1)
else: print(result - 1)
