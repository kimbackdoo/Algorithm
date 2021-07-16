# 처음에는 n//2의 모든 조합을 구하고, 모든 조합에서 2팀씩 조합을 구하려고 했으나 메모리 초과
# n//2의 모든 조합을 구하고, 모든 조합의 경우를 계산했으나 시간초과
# n//2의 모든 조합에서 차례대로 처음과 끝 요소의 팀만 팀을 형성할 수 있으므로 이것을 이용
# 예를 들어, [1, 2, 3, 4, 5, 6]이라면 1번 팀은 6번 팀, 2번 팀은 5번 팀, 3번 팀은 4번 팀으로만 팀을 만들 수 있음

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

numbers = [i for i in range(n)]
team = list(combinations(numbers, n//2)) # 팀을 만들 수 있는 모든 조합, numbers가 오름차순 정렬되어 있으므로 team도 오름차순 정렬 되어 있음

result = 101
for p in range(len(team) // 2): # 처음과 끝 요소만 확인하므로 처음부터 중간까지만 계산하면 됨
  q = -p-1 # 끝 요소 인덱스
  tmp1, tmp2 = 0, 0
  for i in range(n // 2): # team의 모든 요소를 계산하기 위해 반복
    for j in range(n // 2):
      tmp1 += s[team[p][i]][team[p][j]] # tmp1에 하나의 팀 능력치의 합 계산
      tmp2 += s[team[q][i]][team[q][j]] # tmp2에 두번째 팀 능력치의 합 계산

  result = min(result, abs(tmp1 - tmp2)) # result에 최솟값을 저장

print(result)
