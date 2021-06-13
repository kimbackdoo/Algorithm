# def solution(n):
#     # [::-1] : 역순으로 뒤집음
#     # n을 문자열로 변환 후 역순으로 뒤집은 후 map을 이용하여 문자열로 변환된 s의 각 요소를 int로 묶은 후 리스트로 변환
#     return list(map(int, str(n)[::-1]))

def mapping(data_type, arr): # map 함수 
    result = []
    for a in arr:
        result.append(data_type(a))
        
    return result

def solution(n):
    answer = str(n)
    return mapping(int, answer[::-1])
