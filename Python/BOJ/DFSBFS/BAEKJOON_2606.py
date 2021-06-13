from collections import deque

n = int(input())
m = int(input())

matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

visited = [False] * (n+1)

def bfs(v):
  queue = deque([v])
  visited[v] = True
  cnt = 0
  while queue:
    v = queue.popleft()
    for i in range(1, n+1):
      if not visited[i] and matrix[v][i] == 1:
        queue.append(i)
        visited[i] = True
        cnt += 1
  
  print(cnt)

bfs(1)
