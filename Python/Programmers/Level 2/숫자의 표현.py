# 연속되는 자연수의 합이 n이 되려면 연속되는 자연수 중 제일 작은 수가 n//2보다 작거나 같아야함
# 따라서 모든 수를 탐색하는 것이 아닌 이분탐색 사용하고 마지막에 +1

# 이중 반복문 사용하여 비교
# def solution(n):
#     answer, idx = 0, 1
#     while idx <= n:
#         tmp = 0
#         for i in range(idx, n+1): # idx부터 n까지 연속된 자연수의 합이 n이 되는지 체크
#             tmp += i
#             if tmp > n: # tmp가 n과 같아지지 않고 크다면 break
#                 break
#             elif tmp == n: # tmp가 n과 같아진다면 answer 값 1 증가시키고 break
#                 answer += 1
#                 break
#         idx += 1 # idx값 +1 증가시켜서 연속된 자연수를 모두 파악

#     return answer

def solution(n):
    # 연속되는 자연수 중 제일 작은 수 first, 연속되는 자연수의 합이 되는지 확인하기 위한 check, 연속되는 자연수를 표현할 idx 선언
    first, check, idx = 1, 0, 0
    answer = 0
    while first < (n//2+1):
        check += (first + idx) # check에 first와 idx 값을 더해나감
        idx += 1 # 숫자가 연속해서 커져야하므로 idx += 1
        
        if check >= n: # check가 n보다 크거나 같으몀
            if check == n: # 그 중 check가 n과 같다면 answer += 1
                answer += 1
            first += 1 # first 값 +1
            check, idx = 0, 0 # check, idx 값 초기화
    
    return answer + 1 # 이분 탐색이므로 마지막 n은 체크를 안함 따라서 +1
