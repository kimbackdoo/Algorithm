import re

def solution(new_id):
    answer = new_id.lower() # 1단계
    answer = re.sub('[^a-z0-9-_.]', '', answer) # 2단계
    answer = re.sub('[.]+', '.', answer) # 3단계
    answer = re.sub('^[.]|[.]$', '', answer) # 4단계
    answer = 'a' if answer == "" else answer[:15] # 5, 6단계
    answer = re.sub('[.]$', '', answer) # 6-1 단계
    answer = answer + answer[-1] * (3 - len(answer)) if len(answer) <= 2 else answer # 7단계
    
    return answer
