# 균형잡힌 괄호 문자열인지 확인하는 함수, 올바른 괄호 문자열인지 확인하는 함수, 변환하는 함수로 분리

def check(u): # 올바른 괄호 문자열인지 확인하는 함수
    stack = []
    for b in u:
        if stack and stack[-1] == "(" and b == ")": # 짝을 이룬다면 pop
            stack.pop()
            continue
        
        if b == ")": # stack에 닫힌 괄호 먼저 쌓이면 올바른 괄호 문자열이 될 수 없으므로 False 반환
            return False
        
        stack.append(b)
        
    return stack == [] # stack이 비어 있으면 올바른 괄호 문자열
        
def split(p): # 균형잡힌 문자열인지 확인하는 함수
    cnt = {"(": 0, ")": 0} # 열린괄호와 닫힌괄호를 각각 count할 dict
    for i in range(len(p)):
        cnt[p[i]] += 1 # 각 괄호마다 count
        if cnt["("] == cnt[")"]: # 만약 열린 괄호의 개수와 닫힌 괄호의 개수가 같으면 균형잡힌 괄호 문자열이므로
            return p[:i+1], p[i+1:] # p를 더 이상 분리할 수 없는 균형잡힌 괄호 문자열과 균형잡힌 괄호 문자열로 분리하여 반환

def solution(p):
    if p == "": # 1단계, 빈문자열이면 빈문자열 반환
        return ""
    
    u, v = split(p) # 2단계, u는 더 이상 분리할 수 없는 균형잡힌 괄호 문자열, v는 균형잡힌 괄호 문자열
    if check(u): # 3단계, u가 올바른 괄호 문자열이라면
        return u + solution(v) # 3-1단계, v에 대해 1단계부터 다시 수행한 후 u 뒤에 붙인 후 반환
    else: # 4단계, u가 올바른 괄호 문자열이 아니라면
        tmp = "(" + solution(v) + ")" # 4-1, 4-2, 4-3단계, 빈문자열에 "("을 붙이고, v에 대해 1단계부터 수행한 결과를 이어 붙이고, ")"을 다시 붙임
        # 4-4단계, u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 tmp에 붙임
        # 여기서 괄호 방향을 뒤집는다는 뜻은 문자열을 통째로 reverse 하는 것이 아닌 split한 u의 모든 문자의 방향을 바꾼다는 뜻 즉, ")"면 "("로, "("면 ")"로 바꾼다는 뜻
        for b in u[1:-1]:
            # 괄호 방향을 뒤집어서 tmp에 붙임
            if b == "(": tmp += ")"
            else: tmp += "("
        
        return tmp # 4-5단계, 생성된 문자열을 반환
