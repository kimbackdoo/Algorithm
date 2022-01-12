# def solution(lottos, win_nums):
#     # 순위 dict
#     rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
#     answer = 0
#     for lotto in lottos:
#         if lotto in win_nums:
#             answer += 1
#     # 최고 순위는 현재 순위에서 0의 개수를 더한 것
#     # 최저 순위는 현재 순위
#     return [rank[answer + lottos.count(0)], rank[answer]]

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1] # 순위 리스트
    answer = len(set(win_nums) & set(lottos)) # 교집합을 이용하여 현재 순위를 구함
    return [rank[answer + lottos.count(0)], rank[answer]]
