# 입력받은 연결된 정점으로 인접리스트를 생성
# 인접리스트를 모두 방문하여 해당 노드의 부모 노드를 찾음, BFS 알고리즘 적용
# 방문하지 않았으면 해당 노드의 자식노드이고, 이미 방문하였으면 해당 노드의 부모 노드가 됨

from collections import deque

n = int(input())
graph = {i: [] for i in range(n+1)}
for _ in range(n-1):
  a, b = map(int, input().split())
  # 인접리스트 구성
  graph[a].append(b)
  graph[b].append(a)

visited = [0] * (n+1)
result = {} # 해당 노드의 부모노드를 저장할 dict
def bfs(v):
  queue = deque()
  queue.append(v)
  visited[v] = 1
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0: # 해당 노드를 방문하지 않았으면 해당 노드의 자식 노드임을 뜻하므로
        queue.append(i)
        visited[i] = 1 # 해당 노드를 방문 처리
      else: # 해당 노드를 이미 방문하였으면 해당 노드의 부모 노드임을 뜻하므로
        result[v] = i # result에 해당 노드의 부모 노드를 저장 

bfs(1)
for i in range(2, n+1): # 2번 노드부터 차례대로 출력
  print(result[i])
