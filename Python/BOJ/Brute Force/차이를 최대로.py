# permutations 모듈을 이용하여 만들 수 있는 모든 경우의 수를 구한 후 문제에 맞게 계산
# 모듈을 사용하지 않는 방법을 떠올리지 못함.. 더 많은 공부 필요

import sys
input = sys.stdin.readline

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

result = 0
for p in set(permutations(numbers, n)): # 만들 수 있는 모든 경우의 수를 구한 후 중복이 있을 수 있으므로 중복을 제거하기 위해 집합으로 변환
  tmp = 0
  for i in range(n-1):
    tmp += abs(p[i] - p[i+1]) # 문제의 식에 맞게 계산

  result = max(result, tmp) # 최대값을 찾음

print(result)
