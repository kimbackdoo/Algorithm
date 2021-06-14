# priorities의 인덱스와 각 요소를 enumerate을 사용하여 묶음
# stack의 첫번째의 첫번째 요소가 priorities의 최대값과 같다면 priorities에서 해당 요소 제거 후 tmp 리스트에 stack의 첫번째 요소를 pop 후 저장
# 같지 않다면 pop후 append
# 튜플 리스트에서 max 함수를 사용하여 첫번째 요소가 모두 같으면 그 다음 요소 체크

# def solution(priorities, location):
#     stack = []
#     for idx, num in enumerate(priorities):
#         stack.append((num, idx))
    
#     tmp = []
#     while stack:
#         if stack[0][0] == max(priorities):
#             priorities.remove(stack[0][0])
#             tmp.append(stack.pop(0))
#         else:
#             p = stack.pop(0)
#             stack.append(p)
    
#     for i in range(len(tmp)):
#         if tmp[i][1] == location:
#             return i+1

# deque 라이브러리를 사용하여 연산 속도 향상
from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque([(v, i) for i, v in enumerate(priorities)])
    while True:
        item = queue.popleft() # 처음 요소부터 pop, 최대값이면 pop 후 append 연산 진행 안함

        if queue and item[0] < max(queue)[0]: # queue가 비어있지 않고 item[0]의 요소가 queue의 max값의 첫번째 요소보다 작다면
            queue.append(item) # 맨 뒤에 append
        else:
            answer += 1
            if item[1] == location: # item[1]이 원하는 location이면 break
                break

    return answer
