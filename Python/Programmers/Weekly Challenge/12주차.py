# 처음에는 그리디 알고리즘 문제인줄 알고 접근했다가 반례 찾음
# dungeons의 크기가 8이고, dungeons의 모든 요소로 만들 수 있는 모든 경우(순열)을 완전탐색하여 최대값을 찾음
# 최대 8!이므로 시간초과 안됨

# # permutations 모듈을 이용하여 문제 해결
# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
#     for p in list(permutations(dungeons, len(dungeons))): # dungeons의 길이만큼 순열을 구하고 모든 요소 순회
#         tmp = k # k 값 copy
#         cnt = 0
#         for d in p:
#             if tmp >= d[0]: # tmp의 값이 d[0] 이상이면 
#                 tmp -= d[1] # tmp값에서 d[1]값을 뺌
#                 cnt += 1 # 카운팅
        
#         answer = max(answer, cnt) # 매 경우마다 최대값을 찾음
    
#     return answer

# permutations 모듈을 사용하지 않고 dfs 백트래킹 알고리즘 사용
# def solution(k, dungeons):
#     def dfs(p, k): # dfs 알고리즘 구현
#         if len(p) == len(dungeons): # 하나의 순열을 구했으면
#             result.append(p) # 모든 경우를 result에 append
#             return # 재귀 탈출
    
#         for i in range(len(dungeons)): # dungeons 모든 요소 순회
#             if not visited[i]: # i번째 요소를 방문하지 않았으면
#                 visited[i] = True # 방문 처리
#                 dfs(p + [dungeons[i]], k) # dfs 탐색
#                 visited[i] = False # 방문 취소
                
#     result = []
#     visited = [False] * len(dungeons)
#     dfs([], k) # dfs 탐색
    
#     answer = set()
#     for res in result: # 모든 순열 순회
#         tmp = k
#         cnt = 0
#         for d in res:
#             if tmp >= d[0]:
#                 tmp -= d[1]
#                 cnt += 1
        
#         answer.add(cnt)
        
#     return max(answer) # answer의 최대값 return

# 모든 순열을 구한 후 count하지 않고, 순열을 구할 때마다 count함
def solution(k, dungeons):
    def dfs(p, k):
        if len(p) == len(dungeons): # 하나의 순열을 구하였으면, 문제 조건대로 count
            cnt = 0
            for d in p:
                if k >= d[0]:
                    k -= d[1]
                    cnt += 1
            
            answer.add(cnt) # count한 모든 숫자 answer에 add
            return
    
        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = True
                dfs(p + [dungeons[i]], k)
                visited[i] = False
                
    result = []
    visited = [False] * len(dungeons)
    answer = set()
    dfs([], k)
    return max(answer) # answer의 최대값 return
