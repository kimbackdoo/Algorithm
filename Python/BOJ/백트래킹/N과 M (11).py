# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 중복해서 뽑을 수 있으므로, dfs 알고리즘을 이용하여 중복 순열 구현
# 중복되는 수열은 있으면 안되므로 딕셔너리를 이용하여 체크

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야하므로 입력받은 수 오름차순 정렬

check = {} # 중복되는 수열을 체크하기 위한 딕셔너리
def dfs(p): # dfs 구현
  if len(p) == m: # p의 길이가 m과 같다면, 즉, m개를 뽑았다면
    result = " ".join(map(str, p)) # p를 문자열로 변환
    if result not in check: # result가 check에 없으면 즉, 중복되지 않으면
      check[result] = 1 # 방문 처리
      print(result) # 출력

    return # 재귀 탈출
  
  for i in range(n): # numbers의 모든 요소 순회
    dfs(p + [numbers[i]]) # dfs 

dfs([])
