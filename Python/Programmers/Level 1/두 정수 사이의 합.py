# def solution(a, b):
#     # sum을 이용하여 a ~ b까지의 모든 합을 반환
#     # a, b의 대소관계가 정해져 있지 않으므로 min, max 이용
#     return sum([num for num in range(min(a, b), max(a, b)+1)])

def solution(a, b):
    # range 함수가 반복가능한 객체를 만들어주기 때문에 for문 없이 바로 sum 함수를 사용해도 됨
    return sum(range(min(a, b), max(a, b) + 1))

def solution(a, b):
    # 1 ~ n 까지의 합 공식: n * (n + 1) // 2
    # a ~ b 까지의 합 공식: (a - b) * (a + b) // 2
    # a, b의 대소가 정해지지 않았으므로 abs 함수 사용
    return (abs(a - b) + 1) * (a + b) // 2
