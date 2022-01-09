# dfs, bfs 알고리즘을 적용하는 기본 문제
# 아래 풀이는 그래프를 인접행렬로 구하여 품, 인접행렬은 공간 낭비가 심하다는 단점이 있음

# from collections import deque

# n, m, v = map(int, input().split())
# matrix = [[0] * (n+1) for _ in range(n + 1)]
# for _ in range(m):
#   a, b = map(int, input().split())
#   matrix[a][b] = matrix[b][a] = 1
# visited = [0] * (n+1)

# def dfs(v, visited):
#   visited[v] = 1
#   print(v, end = ' ')
#   for i in range(1, n+1):
#     if (visited[i] == 0 and matrix[v][i]==1):
#       dfs(i, visited)

# def bfs(v, visited):
#   queue = deque([v])
#   visited[v] = 0
#   while queue:
#     v = queue.popleft()
#     print(v, end = ' ')
#     for i in range(1, n+1):
#       if (visited[i] == 1 and matrix[v][i]==1):
#         queue.append(i)
#         visited[i] = 0

# dfs(v, visited)
# print()
# bfs(v, visited)

# 아래 풀이는 그래프를 인접 리스트를 사용하여 공간 낭비를 없앰

import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n, m, v = map(int, input().split())
graph = defaultdict(list) # defaultdict을 이용하여 인접 리스트 초기 형태를 만듦
for _ in range(m): # 그래프 생성
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for key in graph: # 그래프 정렬
  graph[key].sort()

def dfs(v): # dfs 정의
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v): # bfs 정의
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
