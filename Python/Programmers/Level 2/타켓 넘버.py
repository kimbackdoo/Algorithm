# 각 숫자를 더하거나 뺄 모든 경우를 생각하고 target을 찾음

# def solution(numbers, target):
#     answer = [0] # 초기값 0으로 저장
#     for number in numbers:
#         tmp = []
#         for n in answer: # 각 숫자를 더하거나 뺀 값을 tmp에 저장
#             tmp.append(n+number)
#             tmp.append(n-number)
#         answer = tmp
        
#     return answer.count(target)

# dfs 알고리즘을 이용하여 타켓넘버의 개수를 구함
# def dfs(numbers, target, res, depth): # dfs 알고리즘 구현
#     global answer
    
#     if depth == len(numbers): # depth가 numbers의 크기와 같다면
#         if res == target: # res가 target과 같다면 카운팅
#             answer += 1
#         return # 재귀 탈출
#     # numbers의 모든 수를 더하거나 빼면서 dfs 탐색
#     dfs(numbers, target, res + numbers[depth], depth + 1)
#     dfs(numbers, target, res - numbers[depth], depth + 1)

# def solution(numbers, target):
#     global answer
#     answer = 0
#     dfs(numbers, target, 0, 0) # dfs 탐색
#     return answer

# queue를 이용한 풀이
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # queue 초기값 설정, 첫번째 요소는 인덱스, 두번째 요소는 결과값
    while queue: # queue가 빌때까지 반복
        idx, res = queue.popleft()
        if idx < len(numbers): # idx가 numbers의 크기보다 작다면
            # numbers의 모든 요소 더하거나 빼고 queue에 append
            queue.append((idx + 1, res + numbers[idx]))
            queue.append((idx + 1, res - numbers[idx]))
        elif res == target: # res가 target과 같다면 카운팅
            answer += 1
    
    return answer
