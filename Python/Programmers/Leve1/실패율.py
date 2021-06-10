# def solution(N, stages):
#     tmp = []
#     for n in range(1, N+1): # 실패율 구하기
#         yet, total = 0, 0
#         for stage in stages:
#             if n <= stage:
#                 total += 1
#             if n == stage:
#                 yet += 1
#         tmp.append(yet / total)
    
#     answer = []
#     fail_rate = sorted(tmp, reverse = True) # tmp는 스테이지 번호에 따라 저장되어있음, fail_rate에 tmp 내림차순 정렬
#     for i in range(len(fail_rate)):
#         answer.append(tmp.index(fail_rate[i]) + 1) # tmp에서 fail_rate[i]을 찾고 +1
#         tmp[tmp.index(fail_rate[i])] = 2 # fail_rate[i]에 해당하는 실패율을 tmp에 방문 표시, 같은 스테이지 고려
        
#     return answer

def solution(N, stages):
    lost = []
    total = len(stages)
    for stage in range(1, N+1): # 1 ~ N까지
        cnt = stages.count(stage) # 해당하는 숫자를 stages에서 count

        if cnt == 0: lost.append(0) # 해당 스테이지에 도달한 사람이 없으면 실패율 0
        else: lost.append(cnt/total) # 실패율 구하기
    
        total -= cnt # 해당 스테이지에 도달한 사람 total에서 뺄셈함 이유는 이렇게 하면 다음 스테이지에 도전한 사람 구할 수 있기 때문

    lost_sort = sorted(lost, reverse=True) # 항상 그냥 정렬하는 것이 아닌 copy로 만들것!!
    answer = []
    for i in range(len(lost_sort)):
        answer.append(lost.index(lost_sort[i]) + 1)
        lost[lost.index(lost_sort[i])] = 2

    return answer
