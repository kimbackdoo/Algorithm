# def isnum(s): # s가 숫자로만 이루어졌는지 확인
#     for word in s:
#         try:
#             int(word) # word가 숫자가 아니면
#         except:
#             return False # False 반환
        
#     return True

# def solution(s):
#     # s의 길이가 4 혹은 6이고, 숫자로만 구성되어있으면 True, 아니면 False 반환
#     return (len(s) == 4 or len(s) == 6) and isnum(s)

def solution(s):
    # isdigit() 메소드를 사용하여 s가 숫자인지 판별
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
