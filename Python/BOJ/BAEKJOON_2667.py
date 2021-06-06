n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = 0
result = []
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
  global cnt
  cnt += 1
  visited[x][y] = True

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 1 and not visited[nx][ny]:
        dfs(nx, ny)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      cnt = 0
      dfs(i, j)
      result.append(cnt)

print(len(result))
print("\n".join(map(str, sorted(result))))
