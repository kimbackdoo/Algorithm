# 입력받은 그래프가 몇개의 덩어리로 이루어져 있는지 세면 됨, bfs 알고리즘 적용
# bfs 탐색을 하여 덩어리의 개수를 셈

# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())

# matrix = [[] for _ in range(n+1)]
# for _ in range(m):
#   u, v = map(int, sys.stdin.readline().split())
#   matrix[u].append(v)
#   matrix[v].append(u)

# visited = [0] * (n+1)
# def bfs(start):
#   queue = deque()
#   queue.append(start)
#   while queue:
#     start = queue.popleft()
#     for i in matrix[start]:
#       if visited[i] == 0:
#         queue.append(i)
#         visited[i] = 1

# result = 0
# for i in range(1, n+1): # 해당 정점을 방문했는지 안했는지 확인하기 위해, 정점은 1부터
#   if visited[i] == 0: # 방문안했으면
#     bfs(i) # 탐색
#     result += 1

# sys.stdout.write(str(result))

import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list) # graph를 그리기 위해 defaultdict 사용
for _ in range(m): # 그래프 생성
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(v): # bfs 정의
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * (n + 1)
count = 0
for v in range(1, n + 1): # 덩어리의 개수를 세기 위함
  if not visited[v]: # 해당 정점을 방문했는지 안했는지 확인하고, 방문하지 않았으면
    bfs(v) # bfs 탐색
    count += 1 # 덩어리 개수 count

print(count)
