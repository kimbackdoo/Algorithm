from collections import deque

def bfs(x, y):
  move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  queue = deque()
  queue.append((x, y))
  copy[x][y] = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < n and 0 <= ny < n and copy[nx][ny] == 0:
        queue.append((nx, ny))
        copy[nx][ny] = 1

n = int(input())

matrix = []
for _ in range(n):
  matrix.append(list(map(int, input().split())))

result = []
for rain in range(0, 101):
  copy = [[0] * n for _ in range(n)] # rain 이하의 비의 양을 체크하기 위한 copy 리스트
  for i in range(n):
    for j in range(n):
      if matrix[i][j] <= rain: # 해당 비오는 양 이하의 숫자들을 모두 1로 변환
        copy[i][j] = 1

  cnt = 0
  for i in range(n):
    for j in range(n):
      if copy[i][j] == 0:
        bfs(i, j)
        cnt += 1
  result.append(cnt)
  
print(max(result))
