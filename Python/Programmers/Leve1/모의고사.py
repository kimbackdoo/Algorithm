# def solution(answers):
#     fail1 = [1,2,3,4,5] # 리스트 개수 5마다 반복
#     fail2 = [2,1,2,3,2,4,2,5] # 리스트 개수 8마다 반복
#     fail3 = [3,3,1,1,2,2,4,4,5,5] # 리스트 개수 10마다 반복
    
#     cnt1, cnt2, cnt3 = 0, 0, 0
#     for i in range(len(answers)):
#         # 1번, 2번, 3번이 몇 문제씩 맞췄는지 count
#         if answers[i] == fail1[i % 5]: cnt1 += 1 # 5개마다 반복되므로 5로 나눈 나머지로 체크
#         if answers[i] == fail2[i % 8]: cnt2 += 1 # 8개마다 반복되므로 8로 나눈 나머지로 체크
#         if answers[i] == fail3[i % 10]: cnt3 += 1 # 10개마다 반복되므로 10으로 나눈 나머지로 체크
    
#     answer = []
#     # 정답을 제일 많이 맞춘사람 answer에 append
#     if cnt1 == max(cnt1, cnt2, cnt3): answer.append(1)
#     if cnt2 == max(cnt1, cnt2, cnt3): answer.append(2)
#     if cnt3 == max(cnt1, cnt2, cnt3): answer.append(3)
        
#     return sorted(answer) # 가장 높은 점수를 받은 사람이 여럿일 수 있으므로 오름차순 정렬

def solution(answers):
    gg1 = [1, 2, 3, 4, 5]
    gg2 = [2, 1, 2, 3, 2, 4, 2, 5]
    gg3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == gg1[i % len(gg1)]: cnt1 += 1
        if answers[i] == gg2[i % len(gg2)]: cnt2 += 1
        if answers[i] == gg3[i % len(gg3)]: cnt3 += 1

    answer = []
    tmp = [cnt1, cnt2, cnt3] # 1번, 2번, 3번 사람들이 맞춘 점수를 리스트에 저장
    for person, score in enumerate(tmp): # enumerate을 이용하여 점수와 index 묶음
        if score == max(tmp): # 점수가 가장 높다면
            answer.append(person+1) # 해당 사람 

    return answer
