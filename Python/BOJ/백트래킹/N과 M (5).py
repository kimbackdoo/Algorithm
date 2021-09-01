# 주어진 n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 경우 출력
# 중복되면 안되고 사전 순으로 증가하는 순으로 출력해야함 즉, dfs 알고리즘을 이용하여 순열을 구함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하게 출력해야 하므로 입력 받은 n개의 숫자를 오름차순 정렬

def dfs(p): # dfs 구현
  if len(p) == m: # p의 길이가 m과 같다면 즉, m개를 뽑았다면
    print(*p) # p 출력
    return # 재귀 탈출

  for i in range(n): # numbers의 모든 요소를 이용하여 순열을 만들어야 하므로 numbers 순회
    if numbers[i] not in p: # 중복되지 않아야 하므로 numbers[i]가 p에 포함되어 있지 않아야함
      dfs(p + [numbers[i]]) # dfs 탐색

dfs([])
