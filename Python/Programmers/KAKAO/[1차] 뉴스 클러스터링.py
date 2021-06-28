# 중복 합집합, 중복 교집합을 구현하는 것이 관건
# 중복 교집합은 set1, set2가 겹치는 것 중 count의 개수가 적은 것
# 중복 합집합은 set1, set2가 겹치는 것 중 count의 개수가 큰 것과 set1, set2가 겹치지 않는 것의 합

# def solution(str1, str2):
#     str1 = str1.upper() # 대소문자를 구분하지 않기 때문에 대문자로 변환
#     set1 = [] # 문자인 것만 2개씩 끊어 리스트로 저장
#     for i in range(len(str1)-1):
#         if str1[i].isalpha() and str1[i+1].isalpha(): # 문자인 것만 추출
#             set1.append(str1[i] + str1[i+1])
        
#     str2 = str2.upper() # 대소문자를 구분하지 않기 때문에 대문자로 변환
#     set2 = []
#     for i in range(len(str2)-1): # 문자인 것만 2개씩 끊어 리스트로 저장
#         if str2[i].isalpha() and str2[i+1].isalpha(): # 문자인 것만 추출
#             set2.append(str2[i] + str2[i+1])
            
#     union, intersection = [], []
#     for i in range(len(set1)):
#         # set1의 요소가 set2에 포함되어 있고, set1의 요소가 intersection에 포함되지 않는 경우
#         # 이유는 아래 코드에서 겹치는 부분을 전부 추가하기 때문에 set1 요소가 이미 intersection에 포함되어 있지 않는 경우만 생각해야함
#         if set1[i] in set2 and set1[i] not in intersection:
#             cnt1 = set1.count(set1[i]) # set1에서 set1의 요소를 count
#             cnt2 = set2.count(set1[i]) # set2에서 set2의 요소를 count
#             for j in range(min(cnt1, cnt2)): # cnt1, cnt2 중 작은 것만큼 반복 즉, 중복 교집합 구함
#                 intersection.append(set1[i])
#             for j in range(max(cnt1, cnt2)): # cnt1, cnt2 중 큰 것만큼 반복 즉, 중복 합집합 중 겹치는 부분 구함
#                 union.append(set1[i])
    
#     diff1 = [x for x in set1 if x not in set2] # set1에서 set2에 포함되어 있지 않은 요소들 구함
#     diff2 = [x for x in set2 if x not in set1] # set2에서 set1에 포함되어 있지 않은 요소들 구함
#     for x in diff1+diff2: # 위에서 구한 중복 합집합에 포함되어 있지 않은 요소들 추가
#         union.append(x)
    
#     if len(union) == 0: # 공집합일 경우
#         return 65536
#     else:
#         return int(len(intersection) / len(union) * 65536)
      
def solution(str1, str2):
    # str1, str2 중복 집합 생성(문자만 체크)
    list1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    tmp = set(list1) | set(list2) # list1, list2 합집합 구함
    res1, res2 = [], []
    if tmp: # 합집합이 비어 있지 않다면
        for t in tmp:
            res1.extend([t] * max(list1.count(t), list2.count(t))) # res1에 max 개수만큼 추가 즉, 중복 합집합 구함
            res2.extend([t] * min(list1.count(t), list2.count(t))) # res2에 min 개수만큼 추가 즉, 중복 교집합 구함
    
        return int(len(res2) / len(res1) * 65536) # 자카드 유사도 계산
    else: # 합집합이 비어 있다면
        return 65536 # 65536 반환
