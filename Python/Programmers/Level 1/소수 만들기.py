# from itertools import combinations

# def solution(nums):
#     nums = list(combinations(nums, 3))
    
#     answer = 0
#     for num in nums:
#         for i in range(2, int(sum(num) ** 0.5) + 1): # for 범위 2 ~ int(sum(num) ** 0.5) 까지!!
#             if sum(num) % i == 0:
#                 break
#             elif i == int(sum(num) ** 0.5):
#                 answer += 1
    
#     return answer

# from itertools import combinations

# def check(num): # 소수 판별 함수
#     for d in range(2, int(num ** 0.5) + 1):
#         if not (num % d):
#             return False
    
#     return True

# def solution(nums):
#     answer = map(sum, combinations(nums, 3)) # map 함수를 이용하여 combinations의 모든 결과들을 각각 더함
#     return len(list(filter(lambda x: check(x), answer))) # filter 함수를 이용하여 소수인것만 걸러내고 길이를 구함

# combinations 모듈을 사용하지 않고 백트래킹 알고리즘 사용, dfs 탐색 사용
def dfs(nums, case, pick, idx, depth): # dfs 정의
    global answer
    
    if depth == pick: # depth가 pick와 같다면 즉, pick만큼 뽑았다면
        if check(case): answer += 1 # 소수 판별하고 소수면 count
        return # 재귀 탈출
    
    for i in range(idx, len(nums)): # nums의 모든 요소 순회하면서 모든 경우의 수 탐색
        dfs(nums, case + nums[i], pick, i + 1, depth + 1) # dfs 탐색
    
def check(num): # 소수 판별 함수
    for d in range(2, int(num ** 0.5) + 1):
        if not (num % d):
            return False
    
    return True

def solution(nums):
    global answer
    
    answer = 0
    dfs(nums, 0, 3, 0, 0) # dfs 탐색
    return answer
