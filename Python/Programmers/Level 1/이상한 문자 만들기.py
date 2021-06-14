# def solution(s):
#     s = s.split(" ") # s를 공백을 기준으로 split
#     for i in range(len(s)):
#         tmp = list(s[i]) # 각 문자열을 리스트로 변환
#         for j in range(len(tmp)):
#             if j % 2 == 0: # 짝수 인덱스이면
#                 tmp[j] = tmp[j].upper() # 대문자로
#             else: # 홀수 인덱스 이면
#                 tmp[j] = tmp[j].lower() # 소문자로
#         s[i] = "".join(tmp)
    
#     return " ".join(s) # 공백을 기준으로 join

# def solution(s):
#     answer = []
#     for x in s.split(" "):
#         word = ''
#         for i in range(len(x)):
#             word += (x[i].upper() if i % 2 == 0 else x[i].lower())
#         answer.append(word)
    
#     return " ".join(answer)

# def upper(word): # 소문자 대문자 변환
#     if word.islower(): # 소문자일 경우만 대문자로 변환
#         return chr(ord(word) - 32)
    
#     return word

def lower(word): # 대문자 소문자 변환
    if word.isupper(): # 대문자일 경우만 소문자로 변환
        return chr(ord(word) + 32)

    return word

def solution(s):
    answer = list(s)
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == " ": # 공백이면
            cnt = 0 # cnt 초기화
            continue
        
        if cnt % 2 == 0: answer[i] = upper(answer[i]) # 공백을 기준으로 짝수 인덱스이면 대문자로 변환
        else: answer[i] = lower(answer[i]) # 공백을 기준으로 홀수 인덱스이면 소문자로 변환
        
        cnt += 1
            
    return "".join(answer)
