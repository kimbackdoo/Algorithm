# def solution(a, b): 
#     return sum([i * j for i, j in zip(a, b)]) # zip을 이용하여 곱셈

def solution(a, b):
    return sum([x * y for x, y in zip(a, b)]) # map을 이용하여 곱셈
