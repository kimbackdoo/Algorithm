# 문제에서 제시한 조건을 따라가면 됨

def solution(s):
    cnt, total = 0, 0
    while s != "1": # s가 1이 될 때까지 반복
        cnt += s.count("0") # 제거할 0의 개수 count
        s = s.replace("0", "") # 0 제거
        s = bin(len(s))[2:] # 0 제거후 1의 길이를 2진수 변환
        total += 1 # 변환 횟수 count
    
    return total, cnt
