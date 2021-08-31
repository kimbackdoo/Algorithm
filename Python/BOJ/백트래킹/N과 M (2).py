# 1부터 n까지 m개를 뽑아 만들 수 있는 경우를 출력하면됨
# 중복되지 않아야 하고, 뽑은 수열은 오름차순이어야 하므로 조합

n, m = map(int, input().split())

def dfs(c, idx):
  if len(c) == m: # c의 길이가 m과 같다면 즉, m개를 뽑았다면
    print(*c) # c 출력
    return # 재귀 탈출
  
  for i in range(idx, n + 1): # 뽑은 수열은 오름차순이어야 하므로 for문의 시작 범위를 idx로 설정
    dfs(c + [i], i + 1) # i를 뽑고 중복 없이 오름차순이어야 하므로 dfs 두번째 인자로 i + 1을 넘겨중

dfs([], 1)
