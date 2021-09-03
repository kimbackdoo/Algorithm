# n개의 숫자들 중에서 m개를 뽑아 만들 수 있는 모든 경우를 출력
# 수열은 오름차순 정렬되어 있어야 하므로, dfs 알고리즘을 이용하여 조합 구현
# 중복되는 수열이 있으면 안되므로 딕셔너리를 이용하여 체크
# 사전 순으로 증가하는 순서로 출력해야 하므로 입력 받은 수 오름차순 정렬

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split())) # 사전 순으로 증가하는 순서로 출력해야 하므로 입력 받은 수 오름차순 정렬

check = {} # 중복되는 수열를 체크하기 위한 딕셔너리
def dfs(c, idx): # dfs 구현
  if len(c) == m: # c의 길이가 m과 같다면 즉, m개를 뽑았다면
    result = " ".join(map(str, c)) # c를 문자열로 변환
    if result not in check: # result가 check에 존재하지 않으면 즉, 중복되지 않으면
      check[result] = 1 # 방문 처리
      print(result) # 출력
      
    return # 재귀 탈출
  
  for i in range(idx, n): # numbers의 모든 요소 순회
    dfs(c + [numbers[i]], i + 1) # dfs 탐색, 2번째 인자로 현재 인덱스 + 1값을 넘겨 수열이 오름차순 정렬되게 

dfs([], 0)
