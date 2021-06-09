def bfs(x, y):
  global result
  queue = set([(x, y, board[x][y])])
  while queue:
    x, y, visited = queue.pop()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1]

      if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
        queue.add((nx, ny, visited + board[nx][ny]))
        result = max(result, len(visited) + 1)

  print(result)

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 1
bfs(0, 0)
