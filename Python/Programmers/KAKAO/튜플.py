# s에서 숫자만 추출
# 숫자들을 count하여 제일 높은 숫자부터 저장

# def solution(s):
#     numbers = []
#     tmp = ""
#     for i in range(len(s)): # s에서 숫자만 추출
#         if s[i].isdigit():
#             tmp += s[i] # 숫자가 1 ~ 1000이하의 자연수이므로 하나의 숫자가 나올때까지 + 연산
#         elif s[i] == "}" or s[i] == ",": # s[i]가 } 또는 , 일경우 tmp가 하나의 숫자가 됨
#             if tmp != "": # tmp가 ""이 아닐 경우 숫자 append
#                 numbers.append(tmp)
#             tmp = "" # tmp 초기화
    
#     n_set = set(numbers) # 중복제거
#     counter = {} # 숫자들을 count할 dict
#     for n in n_set:
#         counter[n] = numbers.count(n) # numbers의 숫자 count
    
#     answer = []
#     for t in sorted(counter.items(), key=lambda x : x[1], reverse=True): # 카운팅된 숫자를 기준으로 내림차순 정렬
#         answer.append(int(t[0])) # 첫번째 요소부터 차례대로 append
    
#     return answer

import re
from collections import Counter

def solution(s):
    # 정규식 사용, \d+: 연속되는 숫자, findall(): 모든 숫자를 찾는 함수
    # Counter 모듈을 사용하여 숫자 카운팅
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])) # 카운팅된 숫자를 기준으로 내림차순 정렬 후 첫 번째 요소부터 차례대로 리스트에 저장
