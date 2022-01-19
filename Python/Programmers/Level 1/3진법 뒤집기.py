# def solution(n):
#     tmp = []
#     while n > 0:
#         tmp.append(str(n % 3)) # tmp에 3진수 숫자들을 문자로 변환 후 저장
#         n //= 3
        
#     answer = "".join(tmp) # tmp 리스트 문자열로 변환
#     return int(answer, 3) # int 함수를 통해서 3진수 10진수로 변환

# def solution(n):
#     tmp = []
#     while n > 0: # 10진수 3진수 변환
#         tmp.append(n % 3)
#         n //= 3
    
#     tmp.reverse()
#     answer = 0
#     for i in range(len(tmp)): # 3진수 10진수 변환
#         answer += tmp[i] * (3**i)
        
#     return answer

def convert(n, base): # 진수 변환 함수
    result = ""
    while n:
        result += str(n % base)
        n //= base
    
    return result

def solution(n):
    return int(convert(n, 3), 3) # 3진수로 변환하고 int를 사용하여 다시 10진수로 
