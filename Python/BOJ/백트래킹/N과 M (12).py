# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 중복해서 뽑을 수 있고, 수열은 오름차순 정렬되어 있어야함, 즉, dfs 알고리즘을 이용하여 중복조합 구현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야 하므로 입력받은 수 오름차순 정렬

check = {} # 중복되는 수열을 체크하기 위한 딕셔너리
def dfs(c, idx): # dfs 구현
  if len(c) == m: # c의 길이가 m과 같다면, 즉, m개를 뽑았다면
    result = " ".join(map(str, c)) # c를 문자열로 변환
    if result not in check: # check에 result가 없다면 즉, 중복되지 않으면
      check[result] = 1 # 방문처리
      print(result) # 출력

    return # 재귀 탈출
  
  for i in range(idx, n): # numbers의 모든 요소 순회
    dfs(c + [numbers[i]], i) # dfs 탐색, 2번째 인자로 현재 인덱스의 값을 넘겨주어 중복해서 뽑을 수 있게하고, 수열이 오름차순 정렬되게 함
  
dfs([], 0)
