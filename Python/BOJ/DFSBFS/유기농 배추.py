# 상하좌우 탐색을 하면서 덩어리의 개수를 세면됨, dfs, bfs 알고리즘 적용
# # dfs 풀이
# def dfs(a, b): # dfs 정의
#   if a < 0 or a >= n or b < 0 or b >= m: # 좌표가 범위를 벗어나면 return False
#     return False
#   if matrix[a][b] == 1: # 아직 방문하지 않았으면
#     matrix[a][b] = 0 # 방문 처리
#     # 상하좌우 탐색
#     dfs(a-1, b)
#     dfs(a, b-1)
#     dfs(a+1, b)
#     dfs(a, b+1)
#     return True # 탐색을 마무리 하였으면 True return
#   return False # 기본적으로 False return

# t = int(input())
# for _ in range(t):
#   # 문제 조건대로 입력받고 배추밭 생성
#   m, n, k = map(int, input().split())
#   matrix = [[0] * m for _ in range(n)]

#   for _ in range(k):
#     y, x = map(int, input().split())
#     matrix[x][y] = 1

#   result = 0
#   for i in range(n):
#     for j in range(m):
#       if dfs(i, j) == True: # 배추밭을 전부 확인하고 덩어리의 개수를 count
#         result += 1

#   print(result)

# bfs 풀이
import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y, n, m): # bfs 정의
  move = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상하좌우 정의
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + move[i][0], y + move[i][1] # 상하좌우 탐색
      if 0 <= nx < n and 0 <= ny < m and land[nx][ny]: # 다음 좌표가 범위 안에 있고, 아직 방문하지 않았으면
        land[nx][ny] = 0 # 방문처리
        queue.append((nx, ny))

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  land = [[0] * m for _ in range(n)]
  for _ in range(k):
    c, r = map(int, input().split())
    land[r][c] = 1
  
  answer = 0
  for i in range(n): # 배추밭 전부 탐색하면서 덩어리 개수 count
    for j in range(m):
      if land[i][j]:
        bfs(i, j, n, m)
        answer += 1
  
  print(answer)
