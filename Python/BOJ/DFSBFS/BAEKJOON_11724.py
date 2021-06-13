import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = [[] for _ in range(n+1)]
for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())
  matrix[u].append(v)
  matrix[v].append(u)

visited = [0] * (n+1)
def bfs(start):
  queue = deque()
  queue.append(start)
  while queue:
    start = queue.popleft()
    for i in matrix[start]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = 1

result = 0
for i in range(1, n+1): # 해당 정점을 방문했는지 안했는지 확인하기 위해, 정점은 1부터
  if visited[i] == 0: # 방문안했으면
    bfs(i) # 탐색
    result += 1

sys.stdout.write(str(result))
