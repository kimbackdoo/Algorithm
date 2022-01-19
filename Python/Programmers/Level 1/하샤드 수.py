# def solution(arr):
#     total = sum([int(num) for num in str(arr)]) # 각 자리수 합
#     return arr % total == 0

def solution(x):
    return bool(not x % sum(map(int, str(x)))) # sum, map 함수를 이용하여 각 자리수의 합을 구하고, bool 함수를 이용하여 boolean 값으로 변환
