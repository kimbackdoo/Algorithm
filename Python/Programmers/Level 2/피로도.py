# 최대한 많은 던전을 도는 것이 중요
# 모든 경우를 확인, 순열 사용

# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
#     for p in list(permutations(dungeons, len(dungeons))): # permutations 모듈을 이용하여 모든 순열을 구하고 반복
#         cur, cnt = k, 0
#         for minimum, consum in p: # 던전 탐험
#             if cur >= minimum: # 현재 피로도가 최소 피로도 이상이면
#                 cur -= consum # 현재 피로도에서 소모 피로도 소모
#                 cnt += 1 # 카운팅
#             elif cur < 0: # 현재 피로도가 0보다 작으면 더 이상 던전을 돌 수 없으므로 break
#                 break
        
#         answer = max(answer, cnt) # 최대값을 구함
    
#     return answer

# permutations 모듈을 사용하지 않고, 백트래킹 알고리즘을 사용하여 순열 구함

# def solution(k, dungeons):
#     def dfs(cur, per): # dfs 알고리즘 구현
#         if len(per) == len(dungeons): # dungeons의 크기만큼 뽑았다면
#             cnt = 0
#             for minimum, consum in per: # 던전을 얼마나 도는지 확인
#                 if cnt < 0:
#                     return # cnt가 0보다 작으면 더 이상 던전을 확인할 필요 없으므로 재귀 탈출
                
#                 if cur >= minimum:
#                     cur -= consum
#                     cnt += 1
            
#             answer.append(cnt) # 모든 카운팅값 answer append
#             return # 재귀 탈출
        
#         for i in range(len(dungeons)):
#             if not visited[i]: # i번째 요소를 방문하지 않았으면
#                 visited[i] = True # 방문 처리
#                 dfs(cur, per + [dungeons[i]]) # dfs 탐색
#                 visited[i] = False # 방문 취소
    
#     answer = []
#     visited = [False] * len(dungeons)
#     dfs(k, [])
#     return max(answer)

# 모든 순열을 구하는 것이 아닌 던전을 도는 횟수만 구함

def solution(k, dungeons):
    def dfs(cur, cnt):
        global answer
        
        if cur < 0: # 현재 피로도가 0보다 작으면 더 이상 던전을 확인할 필요 없으므로 재귀 탈출
            return
        
        if answer < cnt: # answer보다 cnt값이 크다면 answer 값 변경, max 함수를 사용하는 것보다 if문이 빠름
            answer = cnt
        
        for i in range(len(dungeons)): # 던전 탐색
            if cur >= dungeons[i][0] and not visited[i]: # 현재 피로도가 해당 던전의 최소 피로도보다 크거나 같고, 아직 방문하지 않았으면
                visited[i] = True # 방문 처리
                dfs(cur - dungeons[i][1], cnt + 1) # dfs 탐색, 현재 피로도에서 소모 피로도를 뺀 값을 인자로 넘겨주어 바로 횟수를 구함
                visited[i] = False # 방문 취소
    
    global answer
    answer = 0
    visited = [False] * len(dungeons)
    dfs(k, 0)
    return answer
