# def lower(s): # 문자열 소문자로 변환
#     result = []
#     for word in s:
#         if ord("A") <= ord(word) < ord("Z"): # word가 대문자라면
#             result.append(chr(ord(word) + 32)) # chr, ord를 이용하여 소문자로 변환 후 result에 append 
#         else:
#             result.append(word) # word가 소문자라면 word result에 append
        
#     return "".join(result) # 리스트를 문자열 변환

def lower(s): # 문자열 소문자로 변환 숏코딩
    result = [chr(ord(word) + 32) if ord("A") <= ord(word) < ord("Z") else word for word in s]
    return "".join(result)

# def count(s, w): # 해당하는 문자 개수 찾기
#     cnt = 0
#     for word in s:
#         if word == w:
#             cnt += 1
    
#     return cnt

def count(s, w): # 해당하는 문자 개수 찾기 숏코딩
    return sum([1 for word in s if word == w])

def solution(s):
    s = lower(s)
    return count(s, "p") == count(s, "y") # if, else를 사용안하고 == 연산자를 활용하여 True, False 반환
