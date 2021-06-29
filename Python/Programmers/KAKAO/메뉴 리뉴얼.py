# 단품으로 이루어진 각 문자열을 오름차순 정렬한 후 course 리스트에 따라 조합 리스트를 생성
# orders의 모든 요소를 순환하면서 해당 조합이 있는지 체크

# from itertools import combinations
# from collections import defaultdict
# import re

# def solution(orders, course):
#     answer = []
#     for c in course: # course의 각 요소만큼 조합을 만듦
#         tmp = defaultdict(int) # 조합이 몇번 나오지는지 count하기 위한 dict
#         for order in orders:
#             order = "".join(sorted(order)) # order 오름차순 정렬, 이유는 AB, BA는 같기 때문
#             combination = list(combinations(order, c)) # c만큼 조합 리스트 생성
#             for combi in combination: # 만들어진 조합 리스트만큼 반복
#                 new = "".join(combi) # 만들어진 조합 리스트의 요소를 str로 변환
#                 o = re.sub("[^"+new+"]", "", order) # 정규식을 사용하여 order에서 new가 아닌 문자 제거
#                 if new == o: # new와 제거된 order이 같다면
#                     tmp[new] += 1 # count
        
#         rtmp = sorted(tmp.items(), key=lambda x : x[1], reverse=True) # 제일 많이 시킨 조합을 추출해야 하므로 역순 정렬
#         if len(rtmp) > 0 and rtmp[0][1] >= 2: # rtmp dict에 요소가 있어야 하고, 많이 시킨 조합이 2개 이상이어야 하므로
#             max = rtmp[0][1] # 역순 정렬을 하였으므로 첫번째 요소를 max로 설정
#             answer.append(rtmp[0][0]) # answer에 append
#             for i in range(1, len(rtmp)): # rtmp를 반복하면서
#                 if max == rtmp[i][1]: # max 값과 같은 요소가 또 있다면 모두 append
#                     answer.append(rtmp[i][0])
    
#     return sorted(answer)
  
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # orders를 순회하면서 c개 조합을 모두 만들고 tmp에 저장
            # 즉, orders의 모든 요소의 c 조합이 tmp에 담김
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp) # Counter 모듈을 이용하여 개수 count
        if len(counter) != 0 and max(counter.values()) != 1: # counter의 요소가 있어야 하고, 최대 값이 2 이상이어야 함
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())] # counter에서 max 값과 같은 요소들의 조합 즉, key 값을 answer에 추가

    return sorted(answer)  
