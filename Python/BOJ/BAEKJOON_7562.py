from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  x, y = map(int, input().split())
  a, b = map(int, input().split())

  matrix = [[0] * n for _ in range(n)]

  move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

  def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 1
    while queue:
      x, y = queue.popleft()
      for i in range(len(move)):
        nx, ny = x + move[i][0], y + move[i][1]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
          queue.append((nx, ny))
          matrix[nx][ny] = matrix[x][y] + 1

  bfs(x, y)
  print(matrix[a][b] - 1)
