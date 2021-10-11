# n개의 송전탑에서 전선들 중 하나를 끊었을 때 두 전력망이 갖게 되는 송전탑의 개수가 최대한 비슷하면 됨
# 전선들 중 하나를 끊는 부분이 문제 핵심, 끊은 이후 bfs 탐색을 통해 두 전력망의 송전탑의 개수를 구하면 됨

# 전선을 하나 끊는 것은 wires에서 n-2개를 고르는 것과 같으므로 combinations을 이용
# from itertools import combinations
# from collections import deque, defaultdict

# def bfs(graph, v, visited): # bfs 알고리즘 구현
#     queue = deque([v])
#     visited[v] = True
#     cnt = 1
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]: # v와 연결된 부분 탐색
#             if not visited[i]: # 방문하지 않았으면
#                 queue.append(i) # queue에 append
#                 visited[i] = True # 방문 처리
#                 cnt += 1 # 송전탑 count
    
#     return cnt

# def solution(n, wires):
#     answer = 100
#     for combi in list(combinations(wires, n - 2)): # combinations을 이용하여 전선을 하나 끊었을 때의 모든 경우를 구하고 모든 요소 순회
#         graph = defaultdict(list) # defaultdict을 이용하여 딕셔너리의 초기값을 리스트로 설정
#         for v1, v2 in combi:
#             # 인접리스트를 이용하여 v1, v2이 연결되었음을 표시
#             graph[v1].append(v2)
#             graph[v2].append(v1)
    
#         visited = [False] * (n + 1)
#         cnt = bfs(graph, combi[0][0], visited) # bfs 탐색 후 송전탑의 개수를 구함
        
#         # cnt는 combi[0][0]과 연결된 송전탑의 개수만 구하므로 끊어진 나머지 송전탑의 개수는 n - cnt가 됨
#         # 즉, 두 송전탑의 차이는 cnt - (n - cnt)이므로 n - cnt * 2가 됨
#         answer = min(answer, abs(n - cnt * 2)) # min을 이용하여 최솟값을 구함
    
#     return answer

# combinations 모듈을 이용하지 않고 단순히 1개를 제외하고 모든 경우를 탐색
# from collections import deque, defaultdict

# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#     cnt = 1
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 cnt += 1
    
#     return cnt

# def solution(n, wires):
#     answer = 100
#     for i in range(n - 1): # wires의 모든 요소 순회
#         graph = defaultdict(list)
#         for v1, v2 in wires:
#             if wires[i] != [v1, v2]: # wires[i]가 끊어진 전선으로 표현, 즉, 끊어지지 않은 남은 부분을 인접리스트로 표현
#                 graph[v1].append(v2)
#                 graph[v2].append(v1)
        
#         visited = [False] * (n + 1)
#         cnt = bfs(graph, v1, visited)
#         answer = min(answer, abs(n - cnt * 2))
    
#     return answer

# wires의 모든 요소를 순회하면서 전선을 끊게 되면서 시간 복잡도 증가
# 개선하기 위하여 인접행렬을 이용하여 전선을 끊는 것을 표현
# from collections import deque, defaultdict

# def bfs(n, graph, v, check):
#     visited = [False] * (n + 1)
#     queue = deque([v])
#     visited[v] = True
#     cnt = 1
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i] and not check[v][i] and not check[i][v]: # i를 방문하지 않았고, 전선이 끊어지지 않았으면 탐색
#                 queue.append(i)
#                 visited[i] = True
#                 cnt += 1
    
#     return cnt

# def solution(n, wires):
#     check = [[False] * (n + 1) for _ in range(n + 1)] # 전선을 끊는 것을 표현하기 위한 인접행렬
#     graph = defaultdict(list)
#     for v1, v2 in wires:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
    
#     answer = 100
#     for v1, v2 in wires:
#         # 전선을 끊는 것을 True로 표현
#         check[v1][v2] = True
#         check[v2][v1] = True
#         cnt = bfs(n, graph, v1, check)
#         answer = min(answer, abs(n - cnt * 2))
#         # bfs 탐색 이후 끊어진 전선을 원상복구
#         check[v1][v2] = False
#         check[v2][v1] = False
    
#     return answer

# 인접행렬은 2차원 리스트이므로 필요없는 공간이 낭비됨, 1차원 리스트를 이용하여 전선이 끊어지는 것을 표현
from collections import deque, defaultdict

def bfs(n, graph, v, check):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i] and not check[i]: # i를 방문하지 않았고, v와 연결된 i가 전선이 끊어지지 않았으면
                queue.append(i)
                visited[i] = True
                cnt += 1
    
    return cnt

def solution(n, wires):
    check = [False] * (n + 1) # 전선을 끊는 것을 표현할 리스트
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    answer = 100
    for v1, v2 in wires:
        check[v2] = True # 전선이 끊어졌으면 True로 표현, v1과 연결된 부분만 bfs 탐색을 진행하므로 v2를 True로 변환하여 전선이 끊어진 것을 표현
        cnt = bfs(n, graph, v1, check)
        answer = min(answer, abs(n - cnt * 2))
        check[v2] = False # 끊어진 전선을 원상복구
    
    return answer
