# 각 기능의 수행속도를 stack에 저장, 이때 다음 기능의 수행속도가 현재 수행속도보다 작거나 같은 경우 저장하지 않음
# 다음 기능의 수행속도가 현재 수행속도보다 작거나 같은 경우는 한번에 배포되기 때문에 그때마다 현재 배포될 개수 +1씩 진행

# def solution(progresses, speeds):
#     answer = []
#     days, cnt = 0, 0
#     while len(progresses):
#         if (progresses[0] + speeds[0] * days) >= 100: # pop(0) 연산을 진행하므로 리스트의 첫번째 기능과 수행속도를 확인
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
#         else:
#             if cnt > 0:
#                 answer.append(cnt) # 배포될 기능 개수 append
#                 cnt = 0
#             days += 1
    
#     answer.append(cnt)
#     return answer

# def solution(progresses, speeds):
#     answer, stack = [], []
#     cnt = 1
#     for i in range(len(progresses)):
#         speed = 0 # 수행 속도 계산하기 위함
#         while progresses[i] < 100: # 각 기능당 수행속도를 계산
#             progresses[i] += speeds[i]
#             speed += 1
        
#         if stack and stack[-1] >= speed: # stack이 비어있지 않고 stack[-1]의 값이 수행속도보다 크거나 값을 경우
#             answer[-1] += 1 # 배포될 기능 개수 +1
#             continue
#         # 첫번째 기능은 다른 기능과 수행속도를 비교 못하므로 append
#         stack.append(speed)
#         answer.append(cnt)
        
#     return answer

import math

def solution(progresses, speeds):
    stack = []
    for i in range(len(progresses)):
        stack.append(math.ceil((100 - progresses[i]) / speeds[i])) # 각 기능이 완료되는 날짜, 반복문으로 계산하지 않고 바로 계산

    answer = [1] # 첫번째 기능은 무조건 배포되므로 answer에 초기값으로 1 저장
    chk = stack[0] # 첫번째 기능은 무조건 배포되므로 비교수로 첫번째 기능이 완료된 날짜를 저장
    for i in range(1, len(stack)):
        if chk >= stack[i]: # 만약 chk가 다른 기능의 날짜를 포함하고 있으면
            answer[-1] += 1 # answer 마지막 값 +1
            continue

        chk = stack[i] # 아니라면 chk 값 변경
        answer.append(1) # 1 추가

    return answer
