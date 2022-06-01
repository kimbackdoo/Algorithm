# "+-*"의 우선순위가 될 수 있는 모든 경우를 구하고, 주어진 문자열에 반영하여 최종 결과값들 중 최대값을 구하면 된다.
# "+-*"의 우선순위가 될 수 있는 모든 경우(순열)는 총 6가지이므로 모듈을 사용하지 않고, 직접 구함
# 주어진 문자열을 연산자와 숫자로 각각 리스트로 변환하고, 해당하는 우선순위에 맞게 결과값을 구함

# import re

# def calc(a, b, op): # 연산자에 따라 값을 처리해주는 calc 함수
#     if op == "+": return a + b
#     elif op == "-": return a - b
#     elif op == "*": return a * b

# def solution(expression):
#     oper = re.sub("[0-9]", " ", expression).split() # re 모듈을 이용하여 숫자를 공백으로 변환 후 split 메소드를 이용하여 연산자 리스트로 변환
#     numbers = re.sub("[-+*]", " ", expression).split() # re 모듈을 이용하여 연산자를 공백으로 변환 후 split 메소드를 이용하여 숫자 리스트로 변환
#     numbers = list(map(int, numbers)) # numbers의 모든 요소는 문자이므로 숫자로 변환
#     answer = 0
#     for priorities in ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]: # 연산자 우선순위가 될 수 있는 모든 경우를 순회
#         # 결과값 중에 최대값을 구해야하므로 oper, numbers 리스트 복사
#         copy_oper = oper[:]
#         copy_numbers = numbers[:]
#         for op in priorities: # 각각의 우선순위 경우에서 모든 연산자 순회
#             while True:
#                 try: # index 메소드는 해당 요소가 없으면 에러를 던지므로 try except 구문 이용
#                     idx = copy_oper.index(op) # op에 해당하는 index 구함
#                     tmp = calc(copy_numbers[idx], copy_numbers[idx + 1], op) # op에 맞는 값 구함
#                     del copy_oper[idx] # 해당 요소는 계산 되었으므로 del
#                     del copy_numbers[idx] # 해당 요소는 계산 되었으므로 del
#                     del copy_numbers[idx] # 해당 요소는 계산 되었으므로 del
#                     copy_numbers.insert(idx, tmp) # 계산된 결과는 copy_numbers에 insert
#                 except: # 해당 요소가 없으면 break
#                     break

#         answer = max(answer, abs(copy_numbers[-1])) # copy_numbers에 남아있는 값이 계산된 결과이므로 해당 값의 절대값을 구하고 max 함수를 이용하여 전체 최대값을 구함
    
#     return answer

# copy_numbers의 요소를 계산하고 del 함수를 사용하지 않고 리스트 덧셈을 이용

# import re

# def calc(a, b, op):
#     if op == "+": return a + b
#     elif op == "-": return a - b
#     elif op == "*": return a * b

# def solution(expression):
#     oper = re.sub("[0-9]", " ", expression).split()
#     numbers = re.sub("[-+*]", " ", expression).split()
#     numbers = list(map(int, numbers))
#     answer = 0
#     for priorities in ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]:
#         copy_oper = oper[:]
#         copy_numbers = numbers[:]
#         for op in priorities:
#             while True:
#                 try:
#                     idx = copy_oper.index(op)
#                     tmp = calc(copy_numbers[idx], copy_numbers[idx + 1], op)
#                     copy_numbers = copy_numbers[:idx] + [tmp] + copy_numbers[idx + 2:] # 리스트 덧셈을 이용하여 계산된 결과를 copy_numbers에 저장
#                     del copy_oper[idx]
#                 except:
#                     break

#         answer = max(answer, abs(copy_numbers[-1]))
    
#     return answer

# index 메소드를 이용하지 않고 정답 구함

import re

def calc(a, b, op):
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b

def solution(expression):
    oper = re.sub("[0-9]", " ", expression).split()
    numbers = re.sub("[-+*]", " ", expression).split()
    numbers = list(map(int, numbers))
    answer = 0
    for priorities in ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]:
        copy_oper = oper[:]
        copy_numbers = numbers[:]
        for op in priorities:
            idx = 0 # 초기 인덱스 설정
            while idx < len(copy_oper): # copy_oper의 모든 요소를 순회할때까지 반복
                if copy_oper[idx] == op: # idx번째 요소의 값이 op랑 같다면
                    tmp = calc(copy_numbers[idx], copy_numbers[idx + 1], op) # 결과 계산
                    copy_numbers = copy_numbers[:idx] + [tmp] + copy_numbers[idx + 2:] # copy_numbers에 결과값 저장
                    del copy_oper[idx] # 해당 요소 삭제
                    idx -= 1 # 요소가 하나 삭제되었으므로 idx값 -1
                
                idx += 1 # if문에 상관없이 idx값 1씩 증가시켜 반복문 순회

        answer = max(answer, abs(copy_numbers[-1]))
    
    return answer
