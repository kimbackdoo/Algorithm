# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     if len(participant) != len(completion): # 길이가 다르다면
#         completion.append("") # completions 뒤에 빈 문자열 추가
    
#     answer = ""
#     for p, c in zip(participant, completion): # zip 이용하여 묶고 반복
#         if p != c: # 중간에 다른 문자열일 경우 완주를 못한 것
#             answer = p
#             break
            
#     return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c: # 중간에 다른 문자열일 경우 완주를 못한 것
            return p
    return participant[-1] # 전부 똑같으면 제일 마지막 사람이 완주를 못한 것
