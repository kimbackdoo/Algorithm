def solution(arr):
    total = sum([int(num) for num in str(arr)]) # 각 자리수 합
    return arr % total == 0
