# nubers에서 부분 요소의 합이 s가 되는 경우의 수를 구하면 됨
# 합이 될 수 있는 모든 조합의 경우의 수를 확인하여 count
# dfs로 코드도 있는데 아직 dfs로는 풀이방법 떠올리지 못함.. 더 많이 공부할 것!

from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(1, len(numbers) + 1):
  tmp = list(map(sum, combinations(numbers, i))) # 합이 될 수 있는 모든 경우를 확인
  result += tmp.count(s) # 합이 s가 되는 것이 있다면 count

print(result)
