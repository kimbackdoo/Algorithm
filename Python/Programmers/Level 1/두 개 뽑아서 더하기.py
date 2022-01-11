# from itertools import combinations

# def solution(numbers):
#     combi = list(combinations(numbers, 2)) # 2개 조합 만들기
#     answer = [a + b for a, b in combi] # 각 조합에 대해 모든 덧셈 구하기
#     answer = list(set(answer)) # 중복값 제거
#     return sorted(answer) # 오름차순 정렬

# from itertools import combinations

# def solution(numbers):
#     answer = list(map(sum, combinations(numbers, 2))) # map을 이용하여 2개 조합 덧셈 리스트 만들기
#     return sorted(list(set(answer))) # 중복제거 및 오름차순 정렬

# from itertools import combinations

# def solution(numbers):
#     return sorted(set(map(sum, combinations(numbers, 2)))) # map 결과는 set으로 만들고 오름차순 정렬

# 백트레킹 풀이, dfs 알고리즘 이용

def solution(numbers):
    def dfs(case, pick, idx): # dfs 정의
        if len(case) == pick: # 뽑은 경우가 pick와 같다면
            answer.add(sum(case)) # answer에 case의 합 추가
            return # 재귀 탈출
        
        for i in range(idx, len(numbers)): # numbers의 모든 요소를 순회하면서 모든 경우 탐색
            dfs(case + [numbers[i]], pick, i + 1) # dfs 탐색
    
    answer = set()
    dfs([], 2, 0)
    return sorted(answer)
