from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1
visited = [0] * (n+1)

def dfs(v, visited):
  visited[v] = 1
  print(v, end = ' ')
  for i in range(1, n+1):
    if (visited[i] == 0 and matrix[v][i]==1):
      dfs(i, visited)

def bfs(v, visited):
  queue = deque([v])
  visited[v] = 0
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in range(1, n+1):
      if (visited[i] == 1 and matrix[v][i]==1):
        queue.append(i)
        visited[i] = 0

dfs(v, visited)
print()
bfs(v, visited)
