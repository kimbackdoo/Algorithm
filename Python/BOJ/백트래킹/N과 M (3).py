# 1부터 n까지 m개를 뽑아 만들 수 있는 모든 경우를 출력하면 됨
# 중복할 수 있으므로 중복순열

n, m = map(int, input().split())

def dfs(p):
  if len(p) == m: # p의 길이가 m과 같다면 즉, m개를 뽑았다면
    print(*p) # p 출력
    return # 재귀 탈출
  
  for i in range(1, n + 1): # 1부터 n까지 만들 수 있는 모든 경우를 탐색
    dfs(p + [i]) # dfs 

dfs([])
