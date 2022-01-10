# 1번 컴퓨터와 연결된 컴퓨터의 개수를 세면됨, bfs 알고리즘 적용

# from collections import deque

# n = int(input())
# m = int(input())

# matrix = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#   a, b = map(int, input().split())
#   matrix[a][b] = matrix[b][a] = 1

# visited = [False] * (n+1)

# def bfs(v):
#   queue = deque([v])
#   visited[v] = True
#   cnt = 0
#   while queue:
#     v = queue.popleft()
#     for i in range(1, n+1):
#       if not visited[i] and matrix[v][i] == 1:
#         queue.append(i)
#         visited[i] = True
#         cnt += 1
  
#   print(cnt)

# bfs(1)

import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n = int(input())
m = int(input())
graph = defaultdict(list) # 그래프를 표현하기 위해 defaultdict 사용
for _ in range(m): # 그래프 생성
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v): # bfs 정의
  queue = deque([v])
  visited[v] = True
  count = 0 # 1번 컴퓨터와 연결된 컴퓨터를 세기 위한 변수, bfs 탐색할때 마다 count
  while queue:
    v = queue.popleft()
    for i in graph[v]: # v와 연결된 컴퓨터 모두 탐색
      if not visited[i]: # 아직 방문하지 않았다면
        queue.append(i)
        visited[i] = True
        count += 1 # count
  
  return count

visited = [False] * (n + 1)
print(bfs(1))
