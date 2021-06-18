# 열린 괄호로 시작해 닫힌 괄호를 만나면 pop 즉, stack 사용

def solution(s):
    stack = []
    for b in s:
        if stack and stack[-1] == "(" and b == ")": # stack이 비어있지 않거나 stack[-1]이 열린 괄호이고, b가 닫힌 괄호이면 올바른 괄호이므로
            stack.pop() # pop
            continue
        
        stack.append(b) # 그렇지 않으면 append
    
    return len(stack) == 0
