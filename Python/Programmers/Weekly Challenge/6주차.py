# 문제에서 주어진 조건대로 정렬시키면 됨
# 승률은 전체 경기 중 이긴 비율을 구하면 됨
# 예를들어, head2head가 "NNWL"이라면 전체 경기는 2, 이긴 횟수는 1이므로 50프로가 됨

# def solution(weights, head2head):
#     answer = [] # 정렬 결과를 담을 리스트
#     for i in range(len(weights)): # weights의 모든 요소 순회
#         total, win, cnt = 0, 0, 0 # 전체 경기 수를 의미하는 total, 이긴 횟수를 의미하는 win, 자신보다 몸무게가 많이 나가는 사람과 이긴 횟수를 의미하는 cnt
#         for j in range(len(weights)): # 위 변수들의 값을 구하기 위하여 head2head 모든 요소 순회
#             if head2head[i][j] != "N": # head2head[i][j]이 N이 아니라면 즉, 경기를 해봤다면
#                 total += 1 # total count
#                 if head2head[i][j] == "W": # 이겼다면
#                     if weights[i] < weights[j]: # 자신보다 몸무게가 많이 나간다면
#                         cnt += 1 # cnt count
#                     win += 1 # win count
        
#         rate = (win / total) * 100 if total else 0 # 경기를 한번도 안해봤을 경우는 total이 0이므로 total값이 0이 아닌 경우에는 승률 계산, 0일 경우 0
#         answer.append((rate, cnt, weights[i], i + 1)) # 구한 값들 answer에 append
    
#     answer = sorted(answer, key=lambda x : (-x[0], -x[1], -x[2], x[3])) # 문제 조건에 맞게 정렬
#     return list(map(lambda x : x[3], answer)) # 내장함수 map을 이용하여 복서의 번호만 mapping

def solution(weights, head2head):
    answer = []
    for i in range(len(weights)):
        total, win, cnt = 0, 0, 0
        for j in range(len(weights)):
            if head2head[i][j] != "N":
                total += 1
                if head2head[i][j] == "W":
                    if weights[i] < weights[j]:
                        cnt += 1
                    win += 1
        
        rate = (win / total) * 100 if total else 0
        answer.append((rate, cnt, weights[i], -(i + 1))) # 복서의 번호만 오름차순, 나머지는 내림차순 정렬이므로 복서의 번호를 음수로 지정하여 append
        
    return list(map(lambda x : -x[3], sorted(answer, reverse=True))) # 역순 정렬하여 한번에 조건대로 정렬 후 복서의 번호만 mapping
