# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 수열이 중복되면 안되고, 사전 순으로 증가하는 순서로 출력해야함
# dfs 알고리즘을 이용하여 순열을 구하면 됨, 이때 방문 처리와 해당 수열이 이미 존재하는지 확인해야함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야하므로 입력받은 n개의 숫자들 오름차순 정렬

check = {} # 중복되는 순열이 있는지 확인하기 위한 딕셔너리
visited = [False] * n # 방문처리를 위한 리스트
def dfs(p): # dfs 구현
  if len(p) == m: # p의 길이가 m과 같다면 즉, m개를 뽑았다면
    result = " ".join(map(str, p)) # p를 공백을 기준으로 문자열로 변환
    if result not in check: # result가 check에 없다면 즉, 중복되지 않으면
      check[result] = 1 # result 방문 처리
      print(result) # result 출력

    return # 재귀 탈출
  
  for i in range(n): # numbers의 모든 요소를 순회
    if not visited[i]: # i번째 요소를 방문하지 않았으면
      visited[i] = True # 방문 처리
      dfs(p + [numbers[i]]) # dfs 탐색
      visited[i] = False # 방문 취소

dfs([])
