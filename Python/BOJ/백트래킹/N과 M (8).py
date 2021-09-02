# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 중복 가능하고, 수열은 오름차순이어야 함 즉, dfs 알고리즘을 이용하여 중복조합을 구하면 됨

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야 하므로 입력받은 n개의 숫자들 오름차순 정렬

def dfs(c, idx): # dfs 구현
  if len(c) == m: # c의 길이가 m과 같다면, 즉, m개를 뽑았다면
    print(*c) # c 출력
    return # 재귀 탈출
  
  for i in range(idx, n): # numbers의 모든 경우를 확인해야 하므로 모든 요소 순회, 중복가능하고, 수열은 오름차순 정렬되어 있어야 하므로 시작점을 idx로 설정
    dfs(c + [numbers[i]], i) # 2번째 인자로 i 값을 넘겨주어 현재 값 이상인 요소만 탐색
  
dfs([], 0)
