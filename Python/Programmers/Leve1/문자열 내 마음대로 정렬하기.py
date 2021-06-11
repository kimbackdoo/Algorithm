# def solution(strings, n):
#     s = []
#     for string in strings:
#         s.append((string[n], string)) # strings 안에 문자들 중 인덱스 n인 요소들과 문자들을 묶어 튜플로 만듦
        
#     return [string[1] for string in sorted(s)] # 정렬한 s에서 문자만 추출하여 리스트 반환

def solution(strings, n):
    return sorted(strings, key=lambda x : (x[n],x)) # lambda를 이용하여 x[n]에 해당하는 x를 오름차순 정렬
