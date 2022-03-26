# 리스트 a의 최솟값과 b의 최대값을 곱하면 누적합을 최솟값으로 만들 수 있음
# 따라서 a의 최소값과 b의 최대값을 구할 때 최적의 해가 나오므로 그리디 알고리즘과 정렬 알고리즘 적용

# def solution(a, b):
#     a.sort() # a 오름차순 정렬
#     b.sort(reverse=True) # b 내림차순 정렬
#     for i in range(len(a)):
#         a[i] *= b[i] # a의 최솟값과 b의 최대값을 곱하여 누적합이 최소가 되게 합
    
#     return sum(a) # 이때 a의 합이 누적합의 최소이므로 a의 합 반환

# lambda식을 이용한 풀이
def solution(a, b):
    return sum(map(lambda x: x[0] * x[1], zip(sorted(a), sorted(b, reverse=True))))
