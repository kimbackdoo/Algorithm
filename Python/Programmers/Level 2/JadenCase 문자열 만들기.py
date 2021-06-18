# s를 공백을 기준으로 split 후 capitalize를 이용하여 첫단어만 대문자로 변환

# def solution(s):
#     s = s.split(" ")
#     for i in range(len(s)):
#         s[i] = s[i].capitalize()
        
#     return " ".join(s)
  
def solution(s):
    return " ".join([word.capitalize() for word in s.split(" ")]) # 리스트 컴프리헨션 이용
