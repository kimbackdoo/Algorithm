# 지도에서 덩어리의 개수를 세면됨, dfs, bfs 알고리즘 적용
# dfs 풀이
# n = int(input())

# graph = []
# for _ in range(n):
#   graph.append(list(map(int, input())))

# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# cnt = 0
# result = []
# visited = [[False] * n for _ in range(n)]

# def dfs(x, y):
#   global cnt
#   cnt += 1
#   visited[x][y] = True

#   for i in range(4):
#     nx, ny = x + dx[i], y + dy[i]
#     if 0 <= nx < n and 0 <= ny < n:
#       if graph[nx][ny] == 1 and not visited[nx][ny]:
#         dfs(nx, ny)

# for i in range(n):
#   for j in range(n):
#     if graph[i][j] == 1 and not visited[i][j]:
#       cnt = 0
#       dfs(i, j)
#       result.append(cnt)

# print(len(result))
# print("\n".join(map(str, sorted(result))))

# bfs 풀이
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y): # bfs 정의
  move = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상하좌우 정의
  queue = deque()
  queue.append((x, y))
  maps[x][y] = 0 # 초기 좌표 방문 처리
  count = 1 # 집의 개수를 셀 변수
  while queue:
    x, y = queue.popleft()
    for i in range(4): # 상하좌우 탐색
      nx, ny = x + move[i][0], y + move[i][1]
      if 0 <= nx < n and 0 <= ny < n and maps[nx][ny]: # 다음 좌표가 범위 안에 있고, 아직 방문하지 않았으면
        maps[nx][ny] = 0 # 방문 처리
        queue.append((nx, ny))
        count += 1 # count
  
  return count

answer = []
for i in range(n): # 지도의 모든 요소 탐색
  for j in range(n):
    if maps[i][j]:
      answer.append(bfs(i, j))

print(len(answer))
print("\n".join(map(str, sorted(answer))))
