# def solution(s):
#     if len(s) % 2 == 0: # 짝수일 경우
#         return s[len(s)//2 - 1 : len(s)//2 + 1] # s 길이 -1 부터 s 길이 +1까지 split
    
#     return s[len(s)//2 : len(s)//2 + 1] # s 길이부터 s 길이 +1까지 split

# def solution(s):
#     return s[(len(s)-1)//2 : len(s)//2+1] # s 길이에서 -1 후 //2 연산부터 s길이 //2 연산 후 +1까지 split

import math

def solution(s):
    # math 모듈을 사용하여 홀수일때는 가운데 글자 한개, 짝수일때는 가운데 글자 2개를 가져옴
    return s[(len(s) - 1) // 2 : math.ceil((len(s) - 1) / 2) + 1]
