# permutations 모듈을 이용하여 순열이 될 수 있는 모든 경우의 수 출력

from itertools import permutations

n = int(input())

numbers = [str(i) for i in range(1, n+1)] # 출력을 위해서 i를 문자열로 변환, numbers는 오름차순 정렬되어 있으므로 만들어진 순열도 오름차순 정렬되어 있음
for p in set(map(" ".join, permutations(numbers, n))):
  print(p)
