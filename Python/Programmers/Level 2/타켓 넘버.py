# 각 숫자를 더하거나 뺄 모든 경우를 생각하고 target을 찾음

def solution(numbers, target):
    answer = [0] # 초기값 0으로 저장
    for number in numbers:
        tmp = []
        for n in answer: # 각 숫자를 더하거나 뺀 값을 tmp에 저장
            tmp.append(n+number)
            tmp.append(n-number)
        answer = tmp
        
    return answer.count(target)
