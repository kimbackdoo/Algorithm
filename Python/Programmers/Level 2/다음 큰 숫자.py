# 문제에 나온 조건 그대로 따라가면 됨

def solution(n):
    # 조건 2에서 n보다 다음 큰 수와 n을 2진수로 변환했을 때 1의 개수가 같아야 하므로 n을 2진수로 변환 후 1의 개수를 저장
    check = bin(n).count("1")
    while True:
        n += 1 # 조건 1
        if check == bin(n).count("1"): # 조건1, 조건2를 만족하는 수 중 제일 작은 수 반환
            return n
