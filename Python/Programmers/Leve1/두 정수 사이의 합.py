def solution(a, b):
    # sum을 이용하여 a ~ b까지의 모든 합을 반환
    # a, b의 대소관계가 정해져 있지 않으므로 min, max 이용
    return sum([num for num in range(min(a, b), max(a, b)+1)])
