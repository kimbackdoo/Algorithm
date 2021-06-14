def solution(a, b): 
    return sum([i * j for i, j in zip(a, b)]) # zip을 이용하여 곱셈
