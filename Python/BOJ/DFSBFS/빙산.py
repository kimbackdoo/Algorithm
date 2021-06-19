# 주어진 빙산을 모두 탐색해야 하므로 BFS 알고리즘 적용
# 빙산을 녹일 BFS, 덩어리 개수를 확인하는 BFS 2개로 구현
# 빙산을 한번 녹인 후, 덩어리 개수가 2개 이상인지 확인하는 작업을 반복

import sys
from collections import deque

def bfs_ice(x, y): # 빙산을 녹일 BFS
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1
  copy[x][y] = matrix[x][y] # 덩어리 개수를 확인할 때 사용할 copy 리스트 즉, matrix에서 녹지 않은 빙산을 copy
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < n and 0 <= ny < m:
        # matrix[nx][ny] == 0: 주변에 0이 있을 때 녹기 때문
        # visited[nx][ny] == 0: 현재 시점에서 주변에 0이 있을때만 녹아야함 즉, BFS 탐색을 하면서 녹아서 0이 된것은 현재 시점에서 0이 아닌 것
        # matrix[x][y] > 0: 빙산은 아무리 녹아도 0이기 때문
        if matrix[nx][ny] == 0 and visited[nx][ny] == 0 and matrix[x][y] > 0:
            matrix[x][y] -= 1 # 빙산을 녹임
            copy[x][y] = matrix[x][y] # 현재 빙산의 높이를 copy
        elif matrix[nx][ny] > 0 and visited[nx][ny] == 0: # 빙산의 높이가 있고 방문하지 않았으면
          queue.append((nx, ny)) # 계속해서 BFS 탐색
          visited[nx][ny] = 1 # 방문 표시
          copy[nx][ny] = matrix[nx][ny] # 빙산 높이 copy

def bfs(x, y): # 덩어리 개수를 확인할 BFS
  queue = deque()
  queue.append((x, y))
  copy[x][y] = 0 # 방문 표시
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < n and 0 <= ny < m and copy[nx][ny] > 0: # 좌표가 범위 안에 있고, 빙산의 높이가 있으면
        copy[nx][ny] = 0 # 방문 표시
        queue.append((nx, ny)) # 계속해서 BFS 탐색

n, m = map(int, input().split())

matrix = []
for _ in range(n):
  matrix.append(list(map(int, input().split())))

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0
for i in range(n):
  for j in range(m):
    cnt = 0 # 덩어리 개수를 체크할 변수
    if matrix[i][j] > 0: # 빙산의 높이가 있으면
      # 매번 초기화 시키는 이유는 빙산의 높이는 1, 2, ... 년 계속해서 줄어들기 때문
      # 만약 초기화 시키지 않으면 빙산을 한번 녹이고 2번째부터는 제대로 녹지 않음
      visited = [[0] * m for _ in range(n)]
      copy = [[0] * m for _ in range(n)] # 덩어리 개수를 체크할 리스트, 빙산이 녹을 때마다 덩어리 개수를 체크해야 하므로 매번 초기화
      bfs_ice(i, j)
      result += 1 # 빙산을 녹일때마다 +1
      for k in range(n):
        for l in range(m):
          if copy[k][l] > 0: # 빙산의 높이가 있으면 덩어리 개수 체크
            bfs(k, l)
            cnt += 1
          if cnt >= 2: # 만약 덩어리 개수가 2개 이상으로 나누어지면 result 출력 후 프로그램 종료
            print(result)
            sys.exit()

print(0) # 끝까지 덩어리가 2개 이상으로 나누어지지 않으면 0 출력
