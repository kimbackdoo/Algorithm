# def solution(dartResult):
#     bonus = {"S": 1, "D": 2, "T": 3} # 보너스 점수를 위한 dict
#     option = {"*": 2, "#": -1} # 옵션 점수를 위한 dict
    
#     answer = []
#     score = ""
#     for dart in dartResult:
#         if dart.isalpha(): # dart가 문자라면
#             answer.append(int(score) ** bonus[dart]) # answer에 계산된 점수 추가
#             score = "" # 문자열 초기화
#         elif not dart.isalpha() and not dart.isdigit(): # dart가 문자도 숫자도 아니라면 즉, 옵션이라면
#             if dart == "*" and len(answer) >= 2: # dart가 *이고 answer 길이가 2 이상이라면
#                 answer[-2] *= option[dart] # 그 전 점수에 옵션 점수 계산
                
#             answer[-1] *= option[dart] # 해당 점수에 옵션 점수 계산
#         else:
#             score += dart # 0 ~ 10까지 점수를 처리하기 위해서 문자열로 계산 후 int로 변환
    
#     return sum(answer)

def solution(dartResult):
    options = {"S": 1, "D": 2, "T": 3} # 옵션 dict
    bonus = {"*": 2, "#": -1} # 보너스 dict
    point = "" # 점수 문자열
    answer = []
    for dart in list(dartResult):
        if dart in options: # 문자열 중 옵션이 있으면 계산
            answer.append(int(point) ** options[dart])
            point = ""
        elif dart in bonus: # 문자열 중 보너스가 있으면 계산
            answer[-1] *= bonus[dart]
            if len(answer) >= 2 and dart == "*": # 보너스가 중첩될 경우 계산
                answer[-2] *= 2
        else:
            point += dart # 0~10을 처리하기 위한 문자열

    return sum(answer)
