from collections import deque

n, k = map(int, input().split())

MAX = 10**5
matrix = [0] * (MAX + 1)

dx = [-1, 1, 2]

def bfs(x):
  queue = deque()
  queue.append(x)
  matrix[x] = 1
  cnt = 0
  while queue:
    x = queue.popleft()

    if x == k:
      cnt += 1

    for i in range(3):
      if i == 2: nx = x * dx[i]
      else: nx = x + dx[i]

      if 0 <= nx < MAX+1 and (matrix[nx] == 0 or matrix[nx] >= matrix[x] + 1):
        matrix[nx] = matrix[x] + 1
        queue.append(nx)
  
  print(matrix[k] - 1)
  print(cnt)

bfs(n)
