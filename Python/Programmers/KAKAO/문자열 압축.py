# 문자열 s를 1개, 2개, 3개, ... 단위로 압축 즉, 완전탐색 알고리즘 적용

# def solution(s):
#     answer = 1000 # 문자열의 최대 길이는 1000이므로 초기값 1000 설정
#     for i in range(1, len(s) + 1): # 1부터 len(s)까지 압축
#         result = ""
#         check = []
#         cnt = 1
#         for j in range(0, len(s), i): # i만큼 압축 되어야 하므로 인덱스 증가 크기를 i로 설정
#             if (j + i) <= len(s): # (j + i)는 s의 길이보다 작거나 같아야함
#                 tmp = s[j:j+i]
#             else: # s의 길이보다 크다면 tmp에 나머지 문자 저장
#                 tmp = s[j:]

#             if check: # check가 비어있지 않다면
#                 if check[-1] == tmp: # check의 마지막 값이 tmp랑 같다면
#                     cnt += 1 # count
#                     continue

#                 cnt = "" if cnt == 1 else str(cnt) # 같지 않다면 cnt가 1인 것은 생략하므로 1일 때는 빈 문자열, 1이 아닐 때는 cnt를 문자열로 변환
#                 result += (cnt + check[-1]) # result에 압축 결과를 더해나감
#                 cnt = 1 # cnt 값 초기화

#             check.append(tmp) # check에 tmp append
            
#         # 문자열을 압축하고 난 후 마지막 문자를 result에 더함
#         cnt = "" if cnt == 1 else str(cnt)
#         result += (cnt + tmp)

#         if answer > len(result): # 압축 길이가 제일 작은 것을 answer에 저장
#             answer = len(result)

#     return answer

# s의 길이의 절반이 최대 압축할 수 있는 범위, 따라서 s의 길이의 절반을 넘어가게 되면 압축을 할 수 없음
# 따라서 압축 범위는 s 길이의 절반으로 좁힘

def solution(s):
    answer = len(s) # 최대길이가 s의 길이
    for i in range(1, len(s) // 2 + 1): # 압축 범위를 s의 절반으로 좁힘
        result = ""
        check = s[0:i] # 비교할 check 변수의 초기값 설정
        cnt = 1
        for j in range(i, len(s), i):
            if check == s[j:j+i]: # split한 문자열과 check가 같다면 압축할 수 있으므로 count
                cnt += 1
            
            else: # 같지 않다면 압축할 수 없으므로
                result += (str(cnt) + check if cnt > 1 else check) # result에 압축 결과 문자열을 더해나감
                check = s[j:j+i] # check 변수 갱신
                cnt = 1 # count 변수 초기화

        result += (str(cnt) + check if cnt > 1 else check) # 전부 압축하고 마지막 문자열 result에 더함
            
        if answer > len(result):
            answer = len(result)
        
    return answer
