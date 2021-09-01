# 1부터 n까지 m개를 뽑아 만들 수 있는 경우를 출력
# 중복될 수 있으나 수열은 오름차순 정렬되어 있어야함, 즉, dfs 알고리즘을 이용하여 중복조합을 구하면 됨

n, m = map(int, input().split())

def dfs(c, idx): # dfs 구현
  if len(c) == m: # c의 길이가 m이라면 즉, m개를 뽑았다면
    print(*c) # c 출력
    return # 재귀 탈축
  
  for i in range(idx, n + 1): # 중복 가능하고, 오름차순 정렬되어 있어야 하므로 for문의 시작점을 idx로 설정
    dfs(c + [i], i) # dfs 함수의 2번째 인자로 i를 넣어 i 이상의 경우만 구하게 함

dfs([], 1) # dfs 탐색
