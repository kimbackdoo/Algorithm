# def solution(s, n):
#     up, low = [], []
#     for i in range(ord("A"), ord("Z") + 1):
#         up.append(chr(i)) # 알파벳 대문자 리스트 
#         low.append(chr(i + 32)) # 알파벳 소문자 리스트
    
#     answer = ""
#     for word in s:
#         if word == " ":
#             answer += " " # 공백이면 공백 추가
#         # 알파벳 리스트 크기가 26이므로 z 다음 a가 나오게 하기 위해 26으로 나눈 나머지 값을 이용
#         elif ord("A") <= ord(word) <= ord("Z"):
#             # ord(word) - ord("A")는 word가 리스트에서 현재 몇 번째 인덱스인지,
#             # 여기서 +n을 하여 밀린 인덱스를 구하고 리스트 안에서만 값을 찾아야 하므로 26으로 나눔
#             answer += up[(ord(word) - ord("A") + n) % 26]
#         elif ord("a") <= ord(word) <= ord("z"):
#             answer += low[(ord(word) - ord("a") + n) % 26]
    
#     return answer

# def solution(s, n):
#     s = list(s) # s를 리스트로 변환
#     for i in range(len(s)):
#         if s[i].isupper(): # isupper() : 해당 문자가 대문자인지 체크
#             # 위 코드 처럼 알파벳 리스트를 따로 만들지 않고 밀린 인덱스를 구하고 +ord('A')를 하여 A로부터 밀린 암호 문자를 구함
#             # 즉, 아스키코드에서 알파벳 안에서만 암호 문자를 구해낼 수 있음
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
#         elif s[i].islower(): # islower() : 해당 문자가 소문자인지 체크
#             s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

#     return "".join(s)

def solution(s, n):
    # s를 리스트로 변환하지 않고 변수를 두어 계산
    answer = ""
    for i in range(len(s)):
        if s[i].isupper():
            answer += chr((ord(s[i]) + n - ord("A")) % 26 + ord("A"))
        elif s[i].islower():
            answer += chr((ord(s[i]) + n - ord("a")) % 26 + ord("a"))
        else:
            answer += " "
    
    return answer
