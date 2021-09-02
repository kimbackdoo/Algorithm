# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 중복 가능하고, 사전 순으로 증가하는 순서로 출력해야함, 즉, dfs 알고리즘을 이용하여 중복순열을 구하면 됨

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야하므로 입력받은 n개의 숫자를 오름차순 정렬

def dfs(p): # dfs 구현
  if len(p) == m: # p의 길이가 m과 같다면, 즉, m개를 뽑았다면
    print(*p) # p 출력
    return # 재귀 탈출
  
  for i in range(n): # numbers의 모든 경우를 확인해야 하므로 모든 요소 순회
    dfs(p + [numbers[i]]) # dfs 탐색

dfs([])
