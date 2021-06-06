from collections import deque

n, m = map(int, input().split())

matrix = []
for _ in range(n):
  matrix.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 0:
        # 처음 방문한 경우에만 최단 거리 기록
        if matrix[nx][ny] == 1:
          matrix[nx][ny] = matrix[x][y] + 1
          queue.append((nx, ny))
  
  return matrix[n-1][m-1]

print(bfs(0, 0))
