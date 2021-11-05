# 괄호를 0 ~ len(s)-1까지 회전시키면서 올바른 괄호 개수 체크

# def check(s): # 올바른 괄호 체크
#     b = {"(": ")", "{": "}", "[": "]"} # 괄호 짝을 체크하기 위한 dict
#     stack = []
#     for bracket in s:
#         # stack이 비어있지 않고 stack[-1] 값이 열린 괄호로 시작하고, 열린 괄호에 해당하는 닫힌 괄호가 bracket랑 같다면 pop 후 continue
#         # stack[-1] 값이 열린 괄호로 시작하는지를 확인하는 이유는 이렇게 안하면 닫힌 괄호가 stack에 쌓일 수 있음
#         # 예를 들어, "({()})){)" 문자열이 있다면 ")"이 stack에 쌓이게 됨
#         if stack and stack[-1] in "({[" and b[stack[-1]] == bracket:
#             stack.pop()
#             continue
            
#         if bracket in ")}]": # append 전에 s가 닫힌 괄호로 시작한다면 올바른 괄호가 될 수 없기 때문에 바로 False 반환
#             return False
        
#         stack.append(bracket)
        
#     return len(stack) == 0 # stack의 길이가 0이면 올바른 괄호
        

# def solution(s):
#     strings = list(s)
#     answer = 0
#     for _ in range(len(s)):
#         if check(s):
#             answer += 1
            
#         strings.append(strings.pop(0)) # 괄호 회전
#         s = "".join(strings) # 회전 후 괄호 문자열
        
#     return answer

# def check(s): # 들어온 문자열이 올바른 괄호인지 체크
#     dic = {"(":")", "{":"}", "[":"]"} # 열린 괄호로 dict 생성
#     stack = []
#     for i in range(len(s)):
#         # stack이 비어있지 않고, stack[-1] 값이 열린 괄호로 시작하고, 열린 괄호에 해당하는 닫힌 괄호가 s[i]랑 같다면 
#         if stack and stack[-1] in ["(", "{", "["] and dic[stack[-1]] == s[i]:
#             stack.pop() # 값 빼내기
#         else: # 그렇지 않다면
#             stack.append(s[i]) # stack에 추가

#     return len(stack) == 0

# def solution(s):
#     # 리스트 split을 이용하면 괄호 회전을 구할 수 있음 즉, s[i:] + s[:i]
#     return sum([1 for i in range(len(s)) if check(s[i:] + s[:i])]) # 리스트 컴프리헨션 이용

# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         if check(s[i:] + s[:i]):
#             answer += 1

#     return answer

from collections import deque

def check(bracket):
    if bracket[0] in ")}]": return False # 괄호 문자열의 첫번째 요소가 닫힌 괄호이면 올바른 괄호가 아니므로 False return
    
    dic = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for b in bracket:
        if stack and dic[stack[-1]] == b: # stack이 비어있지 않고, stack의 마지막 요소에 해당하는 dic 요소가 b와 같다면 pop
            stack.pop()
            continue
            
        if b in ")}]": return False # 닫힌 괄호 먼저 시작된다면 False return
        
        stack.append(b) # 열린 괄호 append
    
    return False if stack else True
        

def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        s.append(s.popleft()) # 괄호 회전
        if check(s): # 올바른 괄호이면 카운팅
            answer += 1
    
    return answer
