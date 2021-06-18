# 연속되는 자연수의 합이 n이 되려면 연속되는 자연수 중 제일 작은 수가 n//2보다 작거나 같아야함
# 따라서 모든 수를 탐색하는 것이 아닌 이분탐색 사용하고 마지막에 +1

def solution(n):
    # 연속되는 자연수 중 제일 작은 수 first, 연속되는 자연수의 합이 되는지 확인하기 위한 check, 연속되는 자연수를 표현할 idx 선언
    first, check, idx = 1, 0, 0
    answer = 0
    while first < (n//2+1): # 이분탐색
        check += (first + idx) # check에 first와 idx 값을 더해나감
        if check >= n: # check가 n보다 크거나 같으몀
            if check == n: # 그 중 check가 n과 같다면 answer += 1
                answer += 1
            first += 1 # first 값 +1
            check, idx = 0, 0 # check, idx 값 초기화
            continue
            
        idx += 1 # 숫자가 연속해서 커져야하므로 idx += 1
    
    return answer + 1 # 이분 탐색이므로 마지막 n은 체크를 안함 따라서 +1
