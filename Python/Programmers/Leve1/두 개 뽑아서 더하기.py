# from itertools import combinations

# def solution(numbers):
#     combi = list(combinations(numbers, 2)) # 2개 조합 만들기
#     answer = [a + b for a, b in combi] # 각 조합에 대해 모든 덧셈 구하기
#     answer = list(set(answer)) # 중복값 제거
#     return sorted(answer) # 오름차순 정렬

from itertools import combinations

def solution(numbers):
    answer = list(map(sum, combinations(numbers, 2))) # map을 이용하여 2개 조합 덧셈 리스트 만들기
    return sorted(list(set(answer))) # 중복제거 및 오름차순 정렬
