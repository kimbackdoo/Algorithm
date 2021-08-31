# 1부터 n까지 m개를 뽑아 만들 수 있는 모든 순열을 만들면 됨, 단, 중복되면 안됨

n, m = map(int, input().split())

def dfs(p):
  if len(p) == m: # p의 길이가 m과 같으면, 즉, m개를 뽑았으면
    print(*p) # p 출력
    return # 재귀 탈출
  
  for i in range(1, n + 1): # 1부터 n까지 만들 수 있는 모든 경우 탐색
    if i not in p: # i가 p에 없으면, 즉, 중복되지 않으면
      dfs(p + [i]) # dfs 탐색

dfs([])
