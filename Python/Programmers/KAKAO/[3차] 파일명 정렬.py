# 주어진 조건대로 정렬하면됨
# 파일명은 HEAD, NUMBER, TAIL로 이루어져 있는데 문자, 숫자가 섞여 있으므로 HEAD, NUMBER만 추출하는 것이 중요
# HEAD는 대소문자 구분하지 않고 정렬, NUMBER는 숫자로 변환 후 오름차순 정렬하면 됨

# import re

# def solution(files):
#     answer = []
#     for idx, file in enumerate(files): # 입력 시 주어진 파일명 순서대로 정렬해야 하므로 enumerate를 사용하여 index 값 얻음
#         s = re.search("\d+", file) # re 모듈의 search 메소드를 이용하여 NUMBER 부분 검색
#         answer.append((file, file[:s.start()].lower(), int(s.group()), idx)) # answer에 file, HEAD, NUMBER, 초기 순서를 저장
    
#     answer.sort(key=lambda x: (x[1], x[2], x[3])) # HEAD, NUMBER, 초기 순서 순으로 정렬
#     return list(map(lambda x: x[0], answer)) # file만 남겨두고 return

# 리스트가 아닌 딕셔너리를 이용하여 정렬

# import re

# def solution(files):
#     dic = {}
#     for idx, file in enumerate(files):
#         s = re.search("\d+", file)
#         dic[(file[:s.start()].lower(), int(s.group()), idx)] = file # (HEAD, NUMBER, 초기 순서)가 key, file이 value로 저장
    
#     answer = sorted(dic.keys()) # key를 오름차순 정렬
#     return list(map(lambda key: dic[key], answer)) # 정렬한대로 value 값 추출하여 return

# HEAD, NUMBER, 초기 순서 순으로 정렬을 해야 하므로 역으로 NUMBER, HEAD 순으로 정렬해도 똑같음

import re

def solution(files):
    files = sorted(files, key=lambda file: int(re.search("\d+", file).group())) # NUMBER 기준으로 정렬
    return sorted(files, key=lambda file: file[:re.search("\d+", file).start()].lower()) # HEAD 기준으로 정렬하여 return
