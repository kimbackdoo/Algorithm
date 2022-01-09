# (0, 0)에서 출발해서 (n - 1, m - 1)까지 최단거리 경로를 구해야하므로 bfs 알고리즘 적용

# from collections import deque

# n, m = map(int, input().split())

# matrix = []
# for _ in range(n):
#   matrix.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y):
#   queue = deque()
#   queue.append((x, y))
#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 0:
#         # 처음 방문한 경우에만 최단 거리 기록
#         if matrix[nx][ny] == 1:
#           matrix[nx][ny] = matrix[x][y] + 1
#           queue.append((nx, ny))
  
#   return matrix[n-1][m-1]

# print(bfs(0, 0))

import sys
input = sys.stdin.readline

from collections import deque

# 문제 조건대로 입력받음
n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)] # 리스트 컴프리헨션 이용

def bfs(x, y): # bfs 정의
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4): # 상하좌우 확인
      nx, ny = x + move[i][0], y + move[i][1] # nx, ny에 다음 이동할 좌표값 저장
      if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1: # nx, ny가 maps 범위 안에 있고, maps[nx][ny] 값이 1이라면 즉, 아직 방문하지 않았다면
        maps[nx][ny] = maps[x][y] + 1 # maps[nx][ny]에 maps[x][y] + 1 값을 저장하여 최단거리 경로를 구함
        queue.append((nx, ny))
  
move = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상하좌우 확인하기 위한 리스트
bfs(0, 0) # bfs 탐색 시작
print(maps[n - 1][m - 1]) # 결과값 출력
